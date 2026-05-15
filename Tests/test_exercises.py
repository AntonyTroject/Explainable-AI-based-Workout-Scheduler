"""
Unit tests for the exercise database and filtering tool.

These tests verify that filter_exercises() respects session-type tags,
experience-level constraints, physical-limitation safety flags, and
height-based equipment restrictions — the four filters the planner
relies on to produce safe, appropriate exercise pools for each day.
"""

import pytest
from exercises import filter_exercises, EXERCISES, EXP_ORDER


# ──────────────────────────────────────────────────────────────────────
# DATABASE INTEGRITY
# ──────────────────────────────────────────────────────────────────────

class TestDatabaseIntegrity:
    """Sanity checks on the static EXERCISES list itself."""

    def test_database_is_not_empty(self):
        assert len(EXERCISES) > 0

    def test_every_exercise_has_required_fields(self):
        required = {
            "id", "name", "primary", "type", "equipment",
            "min_exp", "knee_safe", "shoulder_safe", "spine_safe", "tags",
        }
        for ex in EXERCISES:
            missing = required - set(ex.keys())
            assert not missing, f"Exercise {ex.get('name')} missing fields: {missing}"

    def test_ids_are_unique(self):
        ids = [ex["id"] for ex in EXERCISES]
        assert len(ids) == len(set(ids))

    def test_safety_flags_are_boolean(self):
        for ex in EXERCISES:
            for flag in ("knee_safe", "shoulder_safe", "spine_safe"):
                assert isinstance(ex[flag], bool), (
                    f"{ex['name']}: {flag} is {type(ex[flag]).__name__}, expected bool"
                )

    def test_min_exp_uses_valid_value(self):
        for ex in EXERCISES:
            assert ex["min_exp"] in EXP_ORDER, (
                f"{ex['name']}: invalid min_exp '{ex['min_exp']}'"
            )


# ──────────────────────────────────────────────────────────────────────
# SESSION-TYPE FILTERING
# ──────────────────────────────────────────────────────────────────────

class TestSessionFiltering:

    def test_push_session_returns_only_push_exercises(self):
        result = filter_exercises("Push", "intermediate")
        assert len(result) > 0
        for ex in result:
            assert "push" in ex["tags"]

    def test_pull_session_returns_only_pull_exercises(self):
        result = filter_exercises("Pull", "intermediate")
        assert len(result) > 0
        for ex in result:
            assert "pull" in ex["tags"]

    def test_legs_session_returns_only_leg_exercises(self):
        result = filter_exercises("Legs", "intermediate")
        assert len(result) > 0
        for ex in result:
            assert "legs" in ex["tags"]

    def test_full_body_session_returns_compound_movements(self):
        result = filter_exercises("Full-Body", "beginner")
        assert len(result) > 0
        for ex in result:
            assert "full" in ex["tags"]


# ──────────────────────────────────────────────────────────────────────
# EXPERIENCE-LEVEL FILTERING
# ──────────────────────────────────────────────────────────────────────

class TestExperienceFiltering:

    def test_beginner_does_not_get_advanced_exercises(self):
        result = filter_exercises("Push", "beginner")
        for ex in result:
            assert ex["min_exp"] == "beginner", (
                f"Beginner received {ex['name']} (min_exp={ex['min_exp']})"
            )

    def test_intermediate_can_get_beginner_and_intermediate(self):
        result = filter_exercises("Push", "intermediate")
        levels = {ex["min_exp"] for ex in result}
        assert levels.issubset({"beginner", "intermediate"})

    def test_advanced_pool_at_least_as_big_as_beginner(self):
        beginner_count = len(filter_exercises("Push", "beginner"))
        advanced_count = len(filter_exercises("Push", "advanced"))
        assert advanced_count >= beginner_count


# ──────────────────────────────────────────────────────────────────────
# LIMITATION HANDLING
# ──────────────────────────────────────────────────────────────────────

class TestLimitationHandling:

    def test_knee_limitation_excludes_knee_unsafe(self):
        with_knee = filter_exercises("Legs", "intermediate", limitations=["knee"])
        for ex in with_knee:
            assert ex["knee_safe"] is True

    def test_shoulder_limitation_excludes_shoulder_unsafe(self):
        with_shoulder = filter_exercises("Push", "intermediate", limitations=["shoulder"])
        for ex in with_shoulder:
            assert ex["shoulder_safe"] is True

    def test_back_limitation_excludes_spine_unsafe(self):
        with_back = filter_exercises("Pull", "intermediate", limitations=["back"])
        for ex in with_back:
            assert ex["spine_safe"] is True

    def test_limitation_reduces_or_keeps_pool_size(self):
        # Adding a limitation should never grow the exercise pool.
        unrestricted = filter_exercises("Push", "intermediate")
        restricted = filter_exercises("Push", "intermediate", limitations=["shoulder"])
        assert len(restricted) <= len(unrestricted)

    def test_no_limitations_argument_defaults_to_empty(self):
        # Passing no limitations should be equivalent to passing [].
        a = filter_exercises("Push", "intermediate")
        b = filter_exercises("Push", "intermediate", limitations=[])
        assert len(a) == len(b)


# ──────────────────────────────────────────────────────────────────────
# HEIGHT-BASED FILTERING
# ──────────────────────────────────────────────────────────────────────

class TestHeightFiltering:
    """Verify that users outside the HEIGHT_BAND don't get fixed-path
    machines unless no alternatives remain."""

    def test_height_within_band_does_not_filter(self):
        normal = filter_exercises("Push", "intermediate", height=180)
        no_height = filter_exercises("Push", "intermediate")
        assert len(normal) == len(no_height)

    def test_height_outside_band_removes_machine_equipment(self):
        # 210 cm is above HEIGHT_BAND_MAX_CM (200), so fixed-path machines
        # should be dropped where alternatives exist.
        tall_user = filter_exercises("Push", "intermediate", height=210)
        # Confirm no machine/hammer equipment slipped through unless it's
        # the only fallback (when nothing else matched the filter).
        normal = filter_exercises("Push", "intermediate")
        if len(tall_user) < len(normal):
            for ex in tall_user:
                assert ex["equipment"] not in ("machine", "hammer")

    def test_height_filter_never_returns_empty_when_unfiltered_has_results(self):
        # Even an extreme height should not collapse the pool to zero
        # when alternatives exist — the function falls back to the
        # original list if filtering would remove everything.
        normal = filter_exercises("Push", "intermediate")
        edge = filter_exercises("Push", "intermediate", height=140)
        assert len(edge) > 0 if len(normal) > 0 else True
