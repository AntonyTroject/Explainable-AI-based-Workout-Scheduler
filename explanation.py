# explanation.py — Algorithm 3.2

import ollama

def generate_explanation(plan: dict) -> str:
    """
    Takes the plan dict from rule_engine.generate_plan()
    and returns a natural-language explanation via Ollama.
    """

    limitations_text = ", ".join(plan["limitations"]) if plan["limitations"] else "none"
    emphasis_text    = plan["emphasis"] if plan["emphasis"] else "none"

    prompt = f"""
You are a certified fitness coach. Explain the following workout plan 
to the user in 4-5 clear sentences. Focus on WHY each parameter was 
chosen based on their profile. Be specific, practical, and encouraging.
Do not use bullet points — write as flowing text.

USER PROFILE:
- Experience level : {plan["experience"]}
- Training goal    : {plan["goal"]}
- Days per week    : {plan["days"]}
- Limitations      : {limitations_text}
- Emphasis         : {emphasis_text}

ASSIGNED PLAN:
- Split            : {plan["split"]}
- Weekly sets/muscle: {plan["volume"][0]}–{plan["volume"][1]}
- Rep range        : {plan["reps"][0]}–{plan["reps"][1]}
- RIR target       : {plan["rir"]}
- Rest between sets: {plan["rest_sec"]} seconds
- Progression rule : {plan["progression"]}

Explain this plan in plain English. Reference the user's specific 
profile values (experience, goal, days) to justify each decision.
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]

    except Exception as e:
        # fallback to template if Ollama is unavailable
        return _template_explanation(plan)


def _template_explanation(plan: dict) -> str:
    """Fallback template-based explanation (Algorithm 3.2 core)."""
    lines = []

    lines.append(
        f"As a {plan['experience']} trainee with {plan['days']} available "
        f"training days per week, a {plan['split']} structure was selected "
        f"to optimize muscle group frequency and recovery."
    )

    lines.append(
        f"A weekly volume of {plan['volume'][0]}–{plan['volume'][1]} sets "
        f"per muscle group was assigned based on your experience level, "
        f"keeping workload within a productive and recoverable range."
    )

    lines.append(
        f"The rep range of {plan['reps'][0]}–{plan['reps'][1]} with "
        f"RIR {plan['rir']} targets your {plan['goal'].replace('_', ' ')} "
        f"goal with appropriate intensity."
    )

    lines.append(
        f"Progression strategy: {plan['progression']}."
    )

    if plan["limitations"]:
        lines.append(
            f"Exercises unsuitable for your limitations "
            f"({', '.join(plan['limitations'])}) have been removed."
        )

    return " ".join(lines)