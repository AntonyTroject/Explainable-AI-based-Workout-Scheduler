# Project Journal

## Step 1 — 24.04

### Planned system and its goal

The system is an **Explainable AI-based Workout Scheduler** — a Python application that generates a personalized weekly resistance-training plan based on the user's profile (experience level, training goal, available days per week, physical limitations, and optional muscle-group emphasis).

Unlike typical fitness apps that present a plan as an opaque output, this system explicitly explains *why* each parameter — split type, weekly volume per muscle, rep range, RIR target, rest interval, progression strategy — was chosen. The goal is to deliver a workout recommendation that is not only individualized and grounded in evidence-based training science, but also fully transparent and pedagogically useful for the user.

### AI / agent-based approach

The system follows a **hybrid AI assistant** architecture combining a deterministic rule-based reasoning core with a generative natural-language layer:

1. **A rule engine** acts as the decision-making component. It maps the user's input profile to training parameters using documented heuristics from strength-training literature (volume targets per muscle group, rep-range/RIR combinations per goal, split selection by available days). All decisions are produced by transparent rules — no machine-learned black box is involved in the recommendation itself, which is what makes the system *explainable by construction*.

2. **An LLM-based explanation tool** (Llama 3 served locally via Ollama) consumes the structured plan and the user profile, then produces a human-readable justification. The LLM does *not* make scheduling decisions; it only verbalizes decisions made by the rule engine.

The assistant receives input from the user, internally calls multiple tools to construct, populate, and explain the plan, and returns a complete weekly schedule together with its rationale.

### Tools used by the system

| Tool | Module | Role |
|------|--------|------|
| **Rule engine** | `rule_engine.py` | Internal tool that maps a user profile dictionary to a structured training plan (split, weekly volumes per muscle, rep range, RIR, rest, progression strategy, per-session volume distribution). |
| **Exercise database & filter** | `exercises.py` | Local structured data store and filter function that returns exercises matching a session type, experience level, and physical-limitation constraints. |
| **LLM API connector** | `explanation.py` → Ollama / Llama 3 | External API tool that produces natural-language justifications from the structured plan. Includes a deterministic template fallback if Ollama is unavailable. |
| **Streamlit web interface** | `app.py` | Input/output handling layer that collects user data through form widgets and presents the generated plan and explanation. |

### Preliminary list of programming concepts

- Modular project architecture and separation of concerns (rules / data / NL generation / UI in distinct files)
- Functions, parameters, return values, and type hints
- Built-in data structures (dictionaries, lists, tuples) for representing plans, volumes, and exercises
- Conditional logic and rule-based branching for the decision engine
- List and dictionary comprehensions for filtering and transformation
- External API integration (Ollama Python client)
- Exception handling and graceful fallback (template explanation when LLM is unavailable)
- String templating and prompt construction for the LLM
- Web user interface with the Streamlit framework
- Version control with Git and project hosting on GitHub
- *(Planned)* Unit testing with `pytest`
- *(Planned)* Dependency management via `requirements.txt`
