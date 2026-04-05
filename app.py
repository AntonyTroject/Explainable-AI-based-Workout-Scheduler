# app.py — Main Streamlit Interface (Section 3.6 from thesis)

import streamlit as st
import random
from rule_engine import generate_plan
from exercises import filter_exercises
from explanation import generate_explanation

# ════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="EXPLAINABLE AI-BASED WORKOUT SCHEDULER",
    page_icon="🏋️",
    layout="wide"
)

# ════════════════════════════════════════════════════════════════════
# SPLIT → SESSION STRUCTURE
# ════════════════════════════════════════════════════════════════════

SPLIT_SESSIONS = {
    "Full-Body":      ["Full-Body", "Full-Body", "Full-Body",
                       "Full-Body", "Full-Body", "Full-Body"],
    "Upper/Lower":    ["Upper", "Lower", "Upper",
                       "Lower", "Upper", "Lower"],
    "Push-Pull-Legs": ["Push", "Pull", "Legs",
                       "Push", "Pull", "Legs"],
    "Split-4":        ["Chest", "Back", "Shoulders",
                       "Arms",  "Legs", "Chest"],
    "Bro-Split":      ["Chest", "Back", "Shoulders",
                       "Arms",  "Legs", "Chest", "Back"],
}

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

EXERCISES_PER_SESSION = {"beginner": 5, "intermediate": 6, "advanced": 7}

# ════════════════════════════════════════════════════════════════════
# BASE MUSCLE GROUPS PER SESSION TYPE
# ════════════════════════════════════════════════════════════════════

# Full-Body base — always cover these
BASE_MUSCLES = ["chest", "back", "shoulders", "biceps", "triceps",
                "quads", "hamstrings"]

# Emphasis → which muscles to prioritize (add extra exercise)
EMPHASIS_MAP = {
    "arms":      ["biceps", "triceps"],
    "legs":      ["quads", "hamstrings", "glutes", "calves"],
    "glutes":    ["glutes", "hamstrings"],
    "shoulders": ["shoulders"],
    "chest":     ["chest"],
    "back":      ["back"],
    "core":      ["core"],
}

def get_target_muscles(plan):
    """Returns ordered list of muscle groups to cover in Full-Body session."""
    base = BASE_MUSCLES.copy()
    emphasis = (plan.get("emphasis") or "").lower().strip()

    extra = []
    for key, muscles in EMPHASIS_MAP.items():
        if key in emphasis:
            extra = muscles
            break

    # add emphasis muscles at front so they get picked first
    final = []
    for m in extra:
        if m not in final:
            final.append(m)
    for m in base:
        if m not in final:
            final.append(m)

    # always add core at end
    if "core" not in final:
        final.append("core")

    return final

# ════════════════════════════════════════════════════════════════════
# SESSION BUILDER
# ════════════════════════════════════════════════════════════════════

def build_sessions(plan):
    sessions_template = SPLIT_SESSIONS[plan["split"]]
    n = plan["days"]
    session_types = sessions_template[:n]

    step = 7 // n
    day_indices = [i * step for i in range(n)]

    sessions = []
    for i, (day_idx, stype) in enumerate(zip(day_indices, session_types)):
        pool = filter_exercises(stype, plan["experience"], plan["limitations"])
        n_ex = EXERCISES_PER_SESSION[plan["experience"]]

        selected = []
        used_muscles = set()

        if stype == "Full-Body":
            target_muscles = get_target_muscles(plan)

            # pick one exercise per target muscle
            for muscle in target_muscles:
                if len(selected) >= n_ex:
                    break
                candidates = [
                    e for e in pool
                    if e["primary"] == muscle
                    and e["primary"] not in used_muscles
                ]
                if candidates:
                    # prefer compound first
                    compounds = [c for c in candidates if c["type"] == "compound"]
                    pick = random.choice(compounds if compounds else candidates)
                    selected.append(pick)
                    used_muscles.add(pick["primary"])

            # fill remaining slots if needed
            if len(selected) < n_ex:
                extras = [
                    e for e in pool
                    if e["primary"] not in used_muscles
                ]
                random.shuffle(extras)
                for e in extras:
                    if len(selected) >= n_ex:
                        break
                    selected.append(e)
                    used_muscles.add(e["primary"])

        else:
            # Push / Pull / Legs / Upper / Lower / Bro-split days
            # pick diverse muscles — one exercise per muscle group
            compound  = [e for e in pool if e["type"] == "compound"]
            isolation = [e for e in pool if e["type"] == "isolation"]
            random.shuffle(compound)
            random.shuffle(isolation)

            for e in compound + isolation:
                if len(selected) >= n_ex:
                    break
                if e["primary"] not in used_muscles:
                    selected.append(e)
                    used_muscles.add(e["primary"])

        # add core every other session (2-3x per week)
        if i % 2 == 0:
            core_pool = filter_exercises(
                "Core", plan["experience"], plan["limitations"]
            )
            if core_pool:
                core_pick = random.choice(core_pool)
                selected.append(core_pick)

        # assign sets / reps / rest to each exercise
        exercises = []
        for ex in selected:
            sets = random.randint(
                max(2, plan["volume"][0] // n),
                max(3, plan["volume"][1] // n)
            )
            sets = max(2, min(sets, 5))
            exercises.append({
                "name":      ex["name"],
                "primary":   ex["primary"],
                "type":      ex["type"],
                "equipment": ex["equipment"],
                "sets":      sets,
                "reps":      f"{plan['reps'][0]}–{plan['reps'][1]}",
                "rir":       plan["rir"],
                "rest":      plan["rest_sec"],
            })

        sessions.append({
            "day":       DAYS_OF_WEEK[day_idx],
            "type":      stype,
            "exercises": exercises,
        })

    return sessions

# ════════════════════════════════════════════════════════════════════
# SIDEBAR — USER INPUT FORM (View 1)
# ════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.title("🏋️ Your Profile")
    st.markdown("---")

    age = st.number_input("Age", min_value=16, max_value=75, value=25)
    sex = st.selectbox("Sex", ["Male", "Female"])

    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("Height (cm)", 140, 220, 175)
    with col2:
        weight = st.number_input("Weight (kg)", 40, 200, 75)

    st.markdown("---")

    experience = st.selectbox(
        "Training Experience",
        ["beginner", "intermediate", "advanced"],
        format_func=lambda x: {
            "beginner":     "🟢 Beginner  (<1 year)",
            "intermediate": "🟡 Intermediate (1–3 years)",
            "advanced":     "🔴 Advanced  (>3 years)"
        }[x]
    )

    goal = st.selectbox(
        "Training Goal",
        ["fat_loss", "recomp", "muscle_gain"],
        format_func=lambda x: {
            "fat_loss":    "🔥 Fat Loss",
            "recomp":      "⚖️  Recomposition",
            "muscle_gain": "💪 Muscle Gain"
        }[x]
    )

    days = st.slider("Training Days / Week", 2, 6, 3)

    st.markdown("---")
    st.markdown("**Optional**")

    limitations = st.multiselect(
        "Physical Limitations",
        ["knee", "shoulder", "back", "elbow"],
        help="Exercises unsuitable for selected limitations will be excluded"
    )

    emphasis = st.text_input(
        "Emphasis (optional)",
        placeholder="e.g. arms, glutes, chest..."
    )

    st.markdown("---")
    generate_btn = st.button("⚡ Generate My Plan", use_container_width=True)

# ════════════════════════════════════════════════════════════════════
# MAIN AREA
# ════════════════════════════════════════════════════════════════════

st.title("🏋️ Explainable AI Workout Scheduler")
st.markdown("*Personalized training plans with transparent reasoning*")
st.markdown("---")

if not generate_btn:
    st.info("👈 Fill in your profile on the left and click **Generate My Plan**")
    st.stop()

# ── GENERATE ─────────────────────────────────────────────────────────
with st.spinner("Generating your plan..."):
    plan = generate_plan(
        experience, days, goal, limitations,
        emphasis if emphasis else None
    )
    sessions = build_sessions(plan)

with st.spinner("Generating AI explanation..."):
    explanation = generate_explanation(plan)

# ════════════════════════════════════════════════════════════════════
# VIEW 2 — PLAN SUMMARY METRICS
# ════════════════════════════════════════════════════════════════════

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Split",         plan["split"])
col2.metric("Days / Week",   f"{plan['days']} days")
col3.metric("Sets / Muscle", f"{plan['volume'][0]}–{plan['volume'][1]}")
col4.metric("Rep Range",     f"{plan['reps'][0]}–{plan['reps'][1]}")
col5.metric("RIR Target",    str(plan["rir"]))

st.markdown("---")
st.subheader("📅 Weekly Training Plan")

# ── SESSION TABLES ────────────────────────────────────────────────────
for s in sessions:
    with st.expander(f"**{s['day']}** — {s['type']}", expanded=True):
        header = st.columns([3, 1, 1, 1, 1, 1])
        header[0].markdown("**Exercise**")
        header[1].markdown("**Muscle**")
        header[2].markdown("**Sets**")
        header[3].markdown("**Reps**")
        header[4].markdown("**RIR**")
        header[5].markdown("**Rest**")

        for ex in s["exercises"]:
            row = st.columns([3, 1, 1, 1, 1, 1])
            badge = "🔵" if ex["type"] == "compound" else "🟣"
            row[0].write(f"{badge} {ex['name']}")
            row[1].write(ex["primary"])
            row[2].write(str(ex["sets"]))
            row[3].write(ex["reps"])
            row[4].write(str(ex["rir"]))
            row[5].write(f"{ex['rest']}s")

# ── REST DAYS ─────────────────────────────────────────────────────────
training_days = {s["day"] for s in sessions}
rest_days = [d for d in DAYS_OF_WEEK if d not in training_days]
if rest_days:
    with st.expander(f"**Rest Days** — {', '.join(rest_days)}"):
        st.write("😴 Recovery — no training scheduled")

# ════════════════════════════════════════════════════════════════════
# VIEW 3 — XAI EXPLANATION BLOCK
# ════════════════════════════════════════════════════════════════════

st.markdown("---")
st.subheader("💡 Why This Plan?")

tag_cols = st.columns(5)
tag_cols[0].markdown(f"`experience: {plan['experience']}`")
tag_cols[1].markdown(f"`goal: {plan['goal']}`")
tag_cols[2].markdown(f"`days: {plan['days']}`")
tag_cols[3].markdown(f"`split: {plan['split']}`")
tag_cols[4].markdown(f"`rir: {plan['rir']}`")

st.markdown(f"> {explanation}")

# ════════════════════════════════════════════════════════════════════
# PROGRESSION STRATEGY
# ════════════════════════════════════════════════════════════════════

st.markdown("---")
st.subheader("📈 Progression Strategy")
st.info(f"**{experience.capitalize()}:** {plan['progression']}")

# ── WARNINGS ──────────────────────────────────────────────────────────
if limitations:
    st.warning(
        f"⚠️ Exercises unsuitable for: **{', '.join(limitations)}** "
        f"have been excluded from all sessions."
    )

if emphasis:
    st.success(
        f"✅ Emphasis applied: **{emphasis}** — "
        f"prioritized in exercise selection."
    )