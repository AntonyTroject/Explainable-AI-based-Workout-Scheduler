# rule_engine.py — Algorithm 3.1

# [beginner_min, beginner_max, intermediate_min, intermediate_max, advanced_min, advanced_max]
NIPPARD_VOLUME = {
    "chest":      [8,  12, 10, 16, 12, 20],
    "back":       [8,  12, 10, 16, 12, 20],
    "shoulders":  [6,  10, 8,  14, 10, 18],
    "biceps":     [6,  10, 8,  14, 10, 16],
    "triceps":    [6,  10, 8,  14, 10, 16],
    "quads":      [8,  12, 10, 16, 12, 20],
    "hamstrings": [6,  10, 8,  14, 10, 16],
    "glutes":     [6,  10, 8,  14, 10, 16],
    "core":       [6,  10, 8,  14, 10, 18],
}

MAIN_MUSCLE_GROUPS = [
    "chest", "back", "shoulders", "biceps", "triceps",
    "quads", "hamstrings", "glutes", "core",
]

SESSION_TOTAL_CAP_BY_EXPERIENCE = {
    "beginner":     30,
    "intermediate": 40,
    "advanced":     50,
}

SPLIT_RULES = {
    ("beginner",     2): "Full-Body",
    ("beginner",     3): "Full-Body",
    ("beginner",     4): "Upper/Lower",
    ("beginner",     5): "Upper/Lower",
    ("intermediate", 2): "Full-Body",
    ("intermediate", 3): "Upper/Lower",
    ("intermediate", 4): "Upper/Lower",
    ("intermediate", 5): "Push-Pull-Legs",
    ("intermediate", 6): "Push-Pull-Legs",
    ("advanced",     3): "Upper/Lower",
    ("advanced",     4): "Push-Pull-Legs",
    ("advanced",     5): "UL-PPL-Hybrid",
    ("advanced",     6): "Push-Pull-Legs",
}

EMPHASIS_MAP = {
    "arms":      ["biceps", "triceps"],
    "legs":      ["quads", "hamstrings", "glutes"],
    "glutes":    ["glutes", "hamstrings"],
    "shoulders": ["shoulders"],
    "chest":     ["chest"],
    "back":      ["back"],
    "core":      ["core"],
}

REP_RANGES = {
    "fat_loss":    (12, 15),
    "recomp":      (10, 14),
    "muscle_gain": (8,  12),
}

RIR_TARGETS = {
    "beginner":     2,
    "intermediate": 1,
    "advanced":     0,
}

REST_SECONDS = {
    "fat_loss":    60,
    "recomp":      90,
    "muscle_gain": 120,
}

_EXP_IDX = {"beginner": 0, "intermediate": 2, "advanced": 4}


def get_split(experience, days):
    return SPLIT_RULES.get((experience, days), "Full-Body")


def get_muscle_volume(muscle, experience, goal, is_emphasis=False):
    if muscle not in NIPPARD_VOLUME:
        return 10
    idx = _EXP_IDX[experience]
    vol_min = NIPPARD_VOLUME[muscle][idx]
    vol_max = NIPPARD_VOLUME[muscle][idx + 1]
    if is_emphasis:
        return vol_max
    return (vol_min + vol_max) // 2


def calculate_weekly_volumes(experience, goal, emphasis=None):
    emphasis_muscles = []
    if emphasis:
        key = emphasis.lower().strip()
        for k, muscles in EMPHASIS_MAP.items():
            if k in key:
                emphasis_muscles = muscles
                break

    volumes = {}
    for muscle in MAIN_MUSCLE_GROUPS:
        volumes[muscle] = get_muscle_volume(
            muscle, experience, goal, is_emphasis=(muscle in emphasis_muscles)
        )
    return volumes, emphasis_muscles


def get_rep_range(goal):
    return REP_RANGES.get(goal, (10, 12))


def get_rir(experience):
    return RIR_TARGETS.get(experience, 2)


def get_rest(goal):
    return REST_SECONDS.get(goal, 90)


def get_progression(experience):
    rules = {
        "beginner":     "Add weight when all reps completed at target RIR for 2 sessions",
        "intermediate": "Double progression: increase reps first, then weight weekly",
        "advanced":     "Periodized blocks: alternate volume and intensity phases",
    }
    return rules.get(experience, "Progressive overload")


def validate_plan_inputs(experience, days, goal, current_weight=None, target_weight=None):
    warnings = []
    if experience == "advanced" and days < 4:
        warnings.append(
            "Advanced trainees need at least 4 training days per week for adequate volume."
        )
    if current_weight is not None and target_weight is not None:
        if goal == "fat_loss" and target_weight > current_weight:
            warnings.append(
                "Target weight is above current weight, which conflicts with a fat loss goal."
            )
        if goal == "muscle_gain" and target_weight < current_weight:
            warnings.append(
                "Target weight is below current weight, which conflicts with a muscle gain goal."
            )
    return warnings


def _distribute_volume(weekly_volumes, days):
    distribution = {i: {} for i in range(days)}
    for muscle, weekly_sets in weekly_volumes.items():
        base = weekly_sets // days
        remainder = weekly_sets % days
        for i in range(days):
            distribution[i][muscle] = base + (1 if i < remainder else 0)
    return distribution


def generate_plan(experience, days, goal, limitations=None, emphasis=None):
    if limitations is None:
        limitations = []

    split = get_split(experience, days)
    weekly_volumes, emphasis_muscles = calculate_weekly_volumes(experience, goal, emphasis)
    rep_min, rep_max = get_rep_range(goal)
    rir = get_rest(goal)
    rest = get_rest(goal)
    progression = get_progression(experience)
    plan_warnings = validate_plan_inputs(experience, days, goal)
    volume_distribution = _distribute_volume(weekly_volumes, days)

    vol_values = list(weekly_volumes.values())

    return {
        "split":               split,
        "experience":          experience,
        "days":                days,
        "goal":                goal,
        "volume":              (min(vol_values), max(vol_values)),
        "reps":                (rep_min, rep_max),
        "rir":                 get_rir(experience),
        "rest_sec":            rest,
        "progression":         progression,
        "limitations":         limitations,
        "emphasis":            emphasis,
        "weekly_volumes":      weekly_volumes,
        "emphasis_muscles":    emphasis_muscles,
        "volume_distribution": volume_distribution,
        "warnings":            plan_warnings,
    }
