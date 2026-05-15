"""
Unit tests for the explanation tool — the LLM-backed natural-language
generation layer.

These tests focus on the deterministic template fallback that runs
when the Ollama service is unavailable. The fallback is what guarantees
the system remains functional and explainable even without a running
LLM, so its correctness is critical.

Live LLM calls are not exercised here: they are non-deterministic,
require a running Ollama daemon, and would make the test suite slow
and flaky. The integration tests in TestLlmErrorHandling patch the
ollama dependency to force the fallback path explicitly.
"""

from unittest.mock import patch

import pytest
from rule_engine import generate_plan
from explanation import generate_explanation, _template_explanation, NUTRITION_REFERENCE


# ──────────────────────────────────────────────────────────────────────
# TEMPLATE FALLBACK
# ──────────────────────────────────────────────────────────────────────

class TestTemplateFallback:
    """Verify the deterministic fallback explanation."""

    def test_template_returns_non_empty_string(self):
        plan = generate_plan("beginner", 3, "muscle_gain")
        text = _template_explanation(plan)
        assert isinstance(text, str)
        assert len(text) > 50

    def test_template_mentions_user_profile_values(self):
        plan = generate_plan("intermediate", 4, "fat_loss")
        text = _template_explanation(plan)
        # The fallback should reference the user's actual profile values.
        assert "intermediate" in text.lower()
        assert "4" in text
        assert plan["split"].lower() in text.lower()

    def test_template_includes_limitations_when_present(self):
        plan = generate_plan("beginner", 3, "recomp", limitations=["knee"])
        text = _template_explanation(plan)
        assert "knee" in text.lower()

    def test_template_omits_limitations_section_when_none(self):
        plan = generate_plan("beginner", 3, "recomp")
        text = _template_explanation(plan)
        # No "limitations" wording should appear when none were set.
        assert "limitation" not in text.lower()

    def test_template_includes_nutrition_note_for_known_goal(self):
        plan = generate_plan("intermediate", 4, "muscle_gain")
        text = _template_explanation(plan)
        # The fallback appends the ISSN nutrition reference for the goal.
        nutrition_fragment = NUTRITION_REFERENCE["muscle_gain"][:30]
        assert nutrition_fragment in text


# ──────────────────────────────────────────────────────────────────────
# LLM ERROR HANDLING
# ──────────────────────────────────────────────────────────────────────

class TestLlmErrorHandling:
    """Verify that LLM failures gracefully fall back to the template."""

    def test_fallback_used_when_ollama_raises_connection_error(self):
        plan = generate_plan("intermediate", 3, "recomp")
        # Force ollama.chat() to raise — simulates daemon down / network error.
        with patch("explanation.ollama.chat", side_effect=ConnectionError("ollama down")):
            result = generate_explanation(plan)
        # generate_explanation should silently fall back to the template.
        assert isinstance(result, str)
        assert len(result) > 0
        assert result == _template_explanation(plan)

    def test_fallback_used_for_arbitrary_exception(self):
        plan = generate_plan("advanced", 4, "muscle_gain")
        with patch("explanation.ollama.chat", side_effect=RuntimeError("boom")):
            result = generate_explanation(plan)
        assert result == _template_explanation(plan)

    def test_successful_llm_response_is_returned_verbatim(self):
        plan = generate_plan("beginner", 3, "recomp")
        fake_response = {"message": {"content": "Mocked explanation text."}}
        with patch("explanation.ollama.chat", return_value=fake_response):
            result = generate_explanation(plan)
        assert result == "Mocked explanation text."


# ──────────────────────────────────────────────────────────────────────
# NUTRITION REFERENCE DATA
# ──────────────────────────────────────────────────────────────────────

class TestNutritionReference:
    """The nutrition reference is a small but visible part of every
    fallback explanation; verify its shape and contents."""

    def test_all_three_goals_have_a_reference(self):
        for goal in ("muscle_gain", "fat_loss", "recomp"):
            assert goal in NUTRITION_REFERENCE
            assert isinstance(NUTRITION_REFERENCE[goal], str)
            assert len(NUTRITION_REFERENCE[goal]) > 0

    def test_each_reference_mentions_protein(self):
        for goal, note in NUTRITION_REFERENCE.items():
            assert "protein" in note.lower(), f"{goal} note missing protein guidance"
