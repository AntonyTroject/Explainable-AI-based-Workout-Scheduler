# Explainable AI-based Workout Scheduler

A Python application that generates a personalised weekly resistance-training plan and produces a natural-language explanation of every decision behind the plan. The system combines a deterministic rule-based decision engine with a Large Language Model (LLM) used purely as a natural-language generation (NLG) layer — the LLM does **not** make scheduling decisions, which is what keeps the system explainable by construction.

---

## What the system does

The user fills in a short profile in the browser — experience level, training goal, available days per week, optional limitations and muscle-group emphasis — and the system returns:

- a weekly **split** (Full-Body, Upper/Lower, PPL, UL-PPL Hybrid),
- a **per-muscle weekly volume** breakdown grounded in the Nippard / Schoenfeld evidence base,
- a **day-by-day session table** with concrete exercises, sets, reps, RIR target and rest interval,
- a **natural-language explanation** of why this plan fits the user,
- a **progression strategy** appropriate to the user's experience.

If a user has a knee, shoulder, back or elbow limitation, unsafe exercises are excluded automatically. If a user's height is outside 150–200 cm, fixed-path machines are deprioritised in favour of free weights and cables. If the LLM service is unavailable, a deterministic template fallback produces the explanation instead, so the system stays functional even offline.

---

## Project structure

```
.
├── app.py              # Streamlit UI — input form, output rendering
├── rule_engine.py      # Rule-based decision engine (the "brain")
├── exercises.py        # Exercise database (74 entries) + filter function
├── explanation.py      # LLM connector + deterministic template fallback
├── tests/              # pytest test suite (55 tests, 0 dependencies on Ollama)
│   ├── test_rule_engine.py
│   ├── test_exercises.py
│   └── test_explanation.py
├── requirements.txt
├── README.md
└── JOURNAL.md          # Course journal (Step 1 / 2 / 3 / Final)
```

Each module has a single responsibility. No module imports the UI, which means the rule engine and the exercise tool can be tested and reused independently of Streamlit.

---

## Installation

### Prerequisites

- **Python 3.10 or newer**
- **Ollama** (optional but recommended) — only needed for live LLM-generated explanations. Without it, the system automatically uses a deterministic template fallback.

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Explainable-AI-based-Workout-Scheduler.git
cd Explainable-AI-based-Workout-Scheduler

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\activate             # Windows

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. (Optional) install and start Ollama for live LLM explanations
#    See https://ollama.com for platform-specific installers.
ollama pull llama3
ollama serve                       # leave running in another terminal
```

---

## Running the application

```bash
streamlit run app.py
```

Streamlit opens the application in your browser (default: http://localhost:8501). Fill in the profile form in the left sidebar and click **Generate My Plan**.

If Ollama is not running, the explanation section will use the deterministic template fallback — every other part of the application is unaffected.

---

## Running the tests

```bash
pytest -v
```

The test suite is self-contained: it does not require a running Ollama daemon, because LLM calls are mocked. Expected output:

```
============================ 55 passed in 0.35s ============================
```

See **JOURNAL.md → Step 3** for a description of what each test scenario covers.

---

## Configuration

No environment variables are required for the default setup. Two values can be overridden in code if needed:

| Variable | Location | Default | Meaning |
|----------|----------|---------|---------|
| LLM model | `explanation.py`, in `ollama.chat(model=...)` | `"llama3"` | Any model previously pulled with `ollama pull`. |
| Ollama host | Ollama daemon | `http://localhost:11434` | Set the `OLLAMA_HOST` environment variable to point at a remote daemon. |

---

## Tools used by the system

| Tool | Module | Role |
|------|--------|------|
| Rule engine | `rule_engine.py` | Maps a user-profile dictionary to a structured plan (split, weekly volume per muscle, rep range, RIR, rest, progression, per-session distribution). All decisions are rule-based — no ML black box is involved. |
| Exercise database & filter | `exercises.py` | Local structured data store of 74 exercises across 11 muscle groups. `filter_exercises()` returns candidates matching the session type, the user's experience, limitations and height. |
| LLM API connector | `explanation.py` (Ollama / Llama 3) | External API tool that produces a human-readable justification of the plan. Includes a deterministic template fallback if the LLM is unavailable. |
| Streamlit UI | `app.py` | Collects user input through form widgets and renders the plan, sessions, and explanation. |

---

## Deployment

The application is designed as a **local web application** for single-user use. The recommended deployment is:

1. The user installs Python and Ollama on their own machine.
2. The user clones the repository and runs `pip install -r requirements.txt`.
3. The user runs `ollama serve` and `streamlit run app.py`.
4. The Streamlit server serves the UI on `localhost:8501`.

Because the LLM runs locally via Ollama, **no user data leaves the machine** — there is no cloud component, no telemetry, and no API key to manage. This is the deliberate default for a health-adjacent application. A future hosted variant could replace the Ollama call with a paid API (OpenAI, Anthropic) without changing the rule engine or the rest of the architecture.

---

## License

Academic project — Riga Technical University, Bachelor's thesis 2025–2026.
