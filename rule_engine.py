# rule_engine.py — Algorithm 3.1 

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
    ("advanced",     5): "Push-Pull-Legs",
    ("advanced",     6): "Split-4",
}

VOLUME_RULES = {
    ("beginner",     "fat_loss"):    (8,  10),
    ("beginner",     "recomp"):      (9,  12),
    ("beginner",     "muscle_gain"): (10, 14),
    ("intermediate", "fat_loss"):    (10, 14),
    ("intermediate", "recomp"):      (12, 16),
    ("intermediate", "muscle_gain"): (14, 20),
    ("advanced",     "fat_loss"):    (12, 16),
    ("advanced",     "recomp"):      (14, 20),
    ("advanced",     "muscle_gain"): (16, 25),
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

def get_split(experience, days):
    return SPLIT_RULES.get((experience, days), "Full-Body")

def get_volume(experience, goal):
    return VOLUME_RULES.get((experience, goal), (10, 15))

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

def generate_plan(experience, days, goal, limitations=[], emphasis=None):
    split      = get_split(experience, days)
    vol_min, vol_max = get_volume(experience, goal)
    rep_min, rep_max = get_rep_range(goal)
    rir        = get_rir(experience)
    rest       = get_rest(goal)
    progression = get_progression(experience)

    return {
        "split":       split,
        "experience":  experience,
        "days":        days,
        "goal":        goal,
        "volume":      (vol_min, vol_max),
        "reps":        (rep_min, rep_max),
        "rir":         rir,
        "rest_sec":    rest,
        "progression": progression,
        "limitations": limitations,
        "emphasis":    emphasis,
    }