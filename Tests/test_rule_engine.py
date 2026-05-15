"""
Unit tests for the rule engine — the deterministic decision-making core.

These tests verify that the rule-based reasoning produces consistent,
literature-grounded outputs for a representative set of user profiles.
They cover split selection, weekly volume calculation, goal-driven
parameter mapping, emphasis handling, input validation, and full plan
integration.
"""

import pytest
from rule_engine import (
    generate_plan,
    get_split,
    get_muscle_volume,
    calculate_weekly_volumes,
    get_rep_range,
    get_rir,
    get_rest,
    get_progression,
    validate_plan_inputs,
    NIPPARD_VOLUME,
    MAIN_MUSCLE_GROUPS,
    SESSION_TOTAL_CAP_BY_EXPERIENCE,
)


# ──────────────────────────────────────────────────────────────────────
# SPLIT SELECTION
# ──────────────────────────────────────────────────────────────────────

class TestSplitSelection:
    """Verify split assignment based on (experience, days_per_week)."""

    def test_beginner_low_frequency_gets_full_body(self):
        assert get_split("beginner", 2) == "Full-Body"
        assert get_split("beginner", 3) == "Full-Body"

    def test_intermediate_four_days_gets_upper_lower(self):
        assert get_split("intermediate", 4) == "Upper/Lower"

    def test_advanced_five_days_gets_hybrid(self):
        # Per SPLIT_RULES, advanced/5-day is the UL-PPL hybrid.
        assert get_split("advanced", 5) == "UL-PPL-Hybrid"

    def test_advanced_six_days_gets_ppl(self):
        # Advanced/6-day is the classic Push-Pull-Legs.
        assert get_split("advanced", 6) == "Push-Pull-Legs"

    def test_unknown_combination_falls_back_to_full_body(self):
        # Any (experience, days) pair outside SPLIT_RULES must default.
        assert get_split("beginner", 99) == "Full-Body"


# ──────────────────────────────────────────────────────────────────────
# VOLUME CALCULATION (Nippard table)
# ──────────────────────────────────────────────────────────────────────

class TestMuscleVolume:
    """Verify weekly volume per muscle stays within Nippard ranges."""

    def test_volume_is_within_nippard_range_for_each_experience(self):
        for muscle in NIPPARD_VOLUME:
            for experience, idx in [("beginner", 0), ("intermediate", 2), ("advanced", 4)]:
                vol_min = NIPPARD_VOLUME[muscle][idx]
                vol_max = NIPPARD_VOLUME[muscle][idx + 1]
                vol = get_muscle_volume(muscle, experience, "recomp")
                assert vol_min <= vol <= vol_max, (
                    f"{muscle}/{experience} produced {vol}, "
                    f"expected in [{vol_min}, {vol_max}]"
                )

    def test_emphasis_returns_max_volume(self):
        # An emphasised muscle should always get the upper end of its range.
        vol_emph = get_muscle_volume("chest", "intermediate", "muscle_gain", is_emphasis=True)
        vol_normal = get_muscle_volume("chest", "intermediate", "muscle_gain", is_emphasis=False)
        assert vol_emph >= vol_normal
        # For intermediate chest: NIPPARD_VOLUME["chest"][3] is the max.
        assert vol_emph == NIPPARD_VOLUME["chest"][3]

    def test_unknown_muscle_falls_back_to_default(self):
        assert get_muscle_volume("unknown_muscle", "beginner", "recomp") == 10


class TestWeeklyVolumes:
    """Verify the per-muscle dictionary returned by calculate_weekly_volumes."""

    def test_all_main_muscle_groups_present(self):
        volumes, _ = calculate_weekly_volumes("intermediate", "muscle_gain")
        for muscle in MAIN_MUSCLE_GROUPS:
            assert muscle in volumes
            assert volumes[muscle] > 0

    def test_arms_emphasis_boosts_biceps_and_triceps(self):
        baseline, _ = calculate_weekly_volumes("intermediate", "recomp")
        boosted, emphasis_muscles = calculate_weekly_volumes(
            "intermediate", "recomp", emphasis="arms"
        )
        assert "biceps" in emphasis_muscles
        assert "triceps" in emphasis_muscles
        assert boosted["biceps"] >= baseline["biceps"]
        assert boosted["triceps"] >= baseline["triceps"]

    def test_no_emphasis_returns_empty_emphasis_list(self):
        _, emphasis_muscles = calculate_weekly_volumes("beginner", "fat_loss")
        assert emphasis_muscles == []


# ──────────────────────────────────────────────────────────────────────
# GOAL-DRIVEN PARAMETERS
# ──────────────────────────────────────────────────────────────────────

class TestGoalParameters:

    def test_rep_ranges_match_goal(self):
        assert get_rep_range("fat_loss") == (12, 15)
        assert get_rep_range("muscle_gain") == (8, 12)

    def test_rir_decreases_with_experience(self):
        # Beginners train further from failure; advanced trainees push closer.
        assert get_rir("beginner") > get_rir("advanced")

    def test_rest_increases_with_strength_focus(self):
        # Heavier work (muscle_gain) → longer rest than fat-loss circuits.
        assert get_rest("muscle_gain") > get_rest("fat_loss")

    def test_progression_string_returned(self):
        for exp in ["beginner", "intermediate", "advanced"]:
            assert isinstance(get_progression(exp), str)
            assert len(get_progression(exp)) > 0


# ──────────────────────────────────────────────────────────────────────
# INPUT VALIDATION
# ──────────────────────────────────────────────────────────────────────

class TestInputValidation:
    """Verify validate_plan_inputs returns appropriate warnings."""

    def test_valid_inputs_produce_no_warnings(self):
        warnings = validate_plan_inputs("intermediate", 4, "muscle_gain", 70, 75)
        assert warnings == []

    def test_too_few_days_for_advanced_warns(self):
        # Advanced trainees need at least 4 days per week.
        warnings = validate_plan_inputs("advanced", 2, "muscle_gain")
        assert len(warnings) > 0
        assert any("training days" in w.lower() for w in warnings)

    def test_fat_loss_with_target_above_current_warns(self):
        warnings = validate_plan_inputs("intermediate", 4, "fat_loss", 70, 80)
        assert any("target" in w.lower() for w in warnings)

    def test_muscle_gain_with_target_below_current_warns(self):
        warnings = validate_plan_inputs("intermediate", 4, "muscle_gain", 80, 70)
        assert any("target" in w.lower() for w in warnings)


# ──────────────────────────────────────────────────────────────────────
# FULL PLAN INTEGRATION
# ──────────────────────────────────────────────────────────────────────

class TestGeneratePlan:
    """End-to-end integration tests for generate_plan()."""

    def test_plan_contains_required_keys(self):
        plan = generate_plan("intermediate", 4, "muscle_gain")
        required = {
            "split", "experience", "days", "goal", "reps", "rir", "rest_sec",
            "progression", "limitations", "emphasis",
            "weekly_volumes", "emphasis_muscles", "volume_distribution",
            "warnings",
        }
        assert required.issubset(plan.keys())

    def test_volume_distribution_covers_all_training_days(self):
        plan = generate_plan("intermediate", 4, "muscle_gain")
        assert len(plan["volume_distribution"]) == 4
        # Keys are session indices 0..days-1
        assert set(plan["volume_distribution"].keys()) == {0, 1, 2, 3}

    def test_weekly_volume_matches_distributed_volume(self):
        # The reported weekly_volumes is recounted from the final distribution
        # after all safety passes; the two should be exactly consistent.
        plan = generate_plan("intermediate", 4, "muscle_gain")
        for muscle, weekly_target in plan["weekly_volumes"].items():
            distributed = sum(
                session.get(muscle, 0)
                for session in plan["volume_distribution"].values()
            )
            assert distributed == weekly_target, (
                f"Muscle {muscle}: weekly={weekly_target}, distributed={distributed}"
            )

    def test_limitations_propagate_into_plan(self):
        plan = generate_plan("beginner", 3, "recomp", limitations=["knee", "shoulder"])
        assert plan["limitations"] == ["knee", "shoulder"]

    def test_per_session_total_respects_experience_cap(self):
        # No session should exceed the per-experience total set cap.
        plan = generate_plan("beginner", 3, "muscle_gain")
        cap = SESSION_TOTAL_CAP_BY_EXPERIENCE["beginner"]
        for session_idx, muscles in plan["volume_distribution"].items():
            assert sum(muscles.values()) <= cap, (
                f"Session {session_idx} has {sum(muscles.values())} sets, "
                f"exceeding cap of {cap}"
            )

    def test_warnings_field_present_and_is_list(self):
        plan = generate_plan("beginner", 3, "recomp")
        assert isinstance(plan["warnings"], list)
