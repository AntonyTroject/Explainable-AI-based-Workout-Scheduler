# exercises.py — Exercise Metadata (Table 3.2)
#
# equipment : barbell | dumbbell | cable | machine | hammer | smith | bodyweight
# tags zone : "push" | "pull" | "upper" | "legs" | "full"
# tags split: "chest" | "back" | "shoulders" | "triceps" | "biceps"
#             "quads" | "hamstrings" | "glutes" | "calves" | "core" | "arms"

EXERCISES = [

    # ── CHEST ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id":  1, "name": "Barbell Bench Press",                "primary": "chest",      "secondary": "triceps",    "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},
    {"id":  2, "name": "Dumbbell Bench Press",               "primary": "chest",      "secondary": "triceps",    "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},
    {"id":  3, "name": "Incline Barbell Bench Press",        "primary": "chest",      "secondary": "shoulders",  "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},
    {"id":  4, "name": "Incline Dumbbell Bench Press",       "primary": "chest",      "secondary": "shoulders",  "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest", "full"]},
    {"id":  5, "name": "Smith Machine Bench Press",          "primary": "chest",      "secondary": "triceps",    "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest", "full"]},
    {"id":  6, "name": "Smith Machine Incline Press",        "primary": "chest",      "secondary": "shoulders",  "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},
    {"id":  7, "name": "Cable Chest Fly",                    "primary": "chest",      "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest", "full"]},
    {"id":  8, "name": "Pec Deck (Butterfly Machine)",       "primary": "chest",      "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest", "full"]},
    {"id":  9, "name": "Dumbbell Fly",                       "primary": "chest",      "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},
    {"id": 10, "name": "Chest Dips (Wide Grip)",             "primary": "chest",      "secondary": "triceps",    "type": "compound",  "equipment": "bodyweight", "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "chest"]},

    # ── BACK ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 11, "name": "Barbell Row",                        "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 12, "name": "Dumbbell Row",                       "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back", "full"]},
    {"id": 13, "name": "Lat Pulldown (Wide Grip)",           "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back", "full"]},
    {"id": 14, "name": "Lat Pulldown (Narrow/Parallel)",     "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back", "full"]},
    {"id": 15, "name": "Cable Pulldown (Crossover)",         "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 16, "name": "Pull-Up (Bodyweight)",               "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "bodyweight", "difficulty": "high",   "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 17, "name": "Weighted Pull-Up",                   "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "bodyweight", "difficulty": "high",   "min_exp": "advanced",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 18, "name": "Cable Row (Seated)",                 "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back", "full"]},
    {"id": 19, "name": "Hammer Strength Low Row",            "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "hammer",     "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back", "full"]},
    {"id": 20, "name": "T-Bar Row (Hammer)",                 "primary": "back",       "secondary": "biceps",     "type": "compound",  "equipment": "hammer",     "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 21, "name": "Cable Pullover",                     "primary": "back",       "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 22, "name": "Barbell Shrug",                      "primary": "back",       "secondary": None,         "type": "isolation", "equipment": "barbell",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 23, "name": "Dumbbell Shrug",                     "primary": "back",       "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},
    {"id": 24, "name": "Smith Machine Shrug",                "primary": "back",       "secondary": None,         "type": "isolation", "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "back"]},

    # ── SHOULDERS ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 25, "name": "Overhead Press (Standing)",          "primary": "shoulders",  "secondary": "triceps",    "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders"]},
    {"id": 26, "name": "Overhead Press (Seated)",            "primary": "shoulders",  "secondary": "triceps",    "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders"]},
    {"id": 27, "name": "Smith Machine Overhead Press",       "primary": "shoulders",  "secondary": "triceps",    "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders", "full"]},
    {"id": 28, "name": "Dumbbell Shoulder Press (Seated)",   "primary": "shoulders",  "secondary": "triceps",    "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders", "full"]},
    {"id": 29, "name": "Lateral Raise (Dumbbell)",           "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders", "full"]},
    {"id": 30, "name": "Lateral Raise (Cable)",              "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "shoulders"]},
    {"id": 31, "name": "Face Pull",                          "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "shoulders"]},
    {"id": 32, "name": "Rear Delt Fly (Dumbbell)",           "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "shoulders"]},
    {"id": 33, "name": "Rear Delt Fly (Cable)",              "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "shoulders"]},
    {"id": 34, "name": "Reverse Pec Deck",                   "primary": "shoulders",  "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "shoulders", "full"]},
    {"id": 35, "name": "Barbell Upright Row",                "primary": "shoulders",  "secondary": "biceps",     "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "shoulders"]},

    # ── TRICEPS ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 36, "name": "Tricep Pushdown (Cable)",            "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms", "full"]},
    {"id": 37, "name": "Skull Crusher (Barbell)",            "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 38, "name": "Skull Crusher (Cable)",              "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 39, "name": "Overhead Tricep Extension (DB)",     "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 40, "name": "Overhead Tricep Ext. (Cable 2-hand)","primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 41, "name": "Overhead Tricep Ext. (Cable 1-hand)","primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 42, "name": "JM Press (Barbell)",                 "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "barbell",    "difficulty": "high",   "min_exp": "advanced",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 43, "name": "JM Press (Smith Machine)",           "primary": "triceps",    "secondary": None,         "type": "isolation", "equipment": "smith",      "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 44, "name": "Close Grip Bench Press (Barbell)",   "primary": "triceps",    "secondary": "chest",      "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},
    {"id": 45, "name": "Close Grip Bench Press (Smith)",     "primary": "triceps",    "secondary": "chest",      "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["push", "upper", "triceps", "arms"]},

    # ── BICEPS ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 46, "name": "Barbell Curl",                       "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "barbell",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms", "full"]},
    {"id": 47, "name": "Dumbbell Curl",                      "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms", "full"]},
    {"id": 48, "name": "Hammer Curl",                        "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms"]},
    {"id": 49, "name": "Preacher Curl (Dumbbell)",           "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms"]},
    {"id": 50, "name": "Preacher Curl (Barbell)",            "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "barbell",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms"]},
    {"id": 51, "name": "Preacher Curl (Machine)",            "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms", "full"]},
    {"id": 52, "name": "Bayesian Curl (Cable)",              "primary": "biceps",     "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["pull", "upper", "biceps", "arms"]},

    # ── QUADS ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 53, "name": "Barbell Squat",                      "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "barbell",    "difficulty": "high",   "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads", "full"]},
    {"id": 54, "name": "Smith Machine Squat",                "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads", "full"]},
    {"id": 55, "name": "Hack Squat (Machine)",               "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads", "full"]},
    {"id": 56, "name": "Leg Press",                          "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads", "full"]},
    {"id": 57, "name": "Bulgarian Split Squat (Dumbbell)",   "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "dumbbell",   "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads"]},
    {"id": 58, "name": "Bulgarian Split Squat (Smith)",      "primary": "quads",      "secondary": "glutes",     "type": "compound",  "equipment": "smith",      "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads"]},
    {"id": 59, "name": "Leg Extension",                      "primary": "quads",      "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": False, "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "quads"]},

    # ── HAMSTRINGS ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 60, "name": "Romanian Deadlift (Barbell)",        "primary": "glutes",     "secondary": "hamstrings", "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "hamstrings", "glutes", "full"]},
    {"id": 61, "name": "Stiff-Leg Deadlift (Barbell)",       "primary": "hamstrings", "secondary": "glutes",     "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "intermediate", "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "hamstrings"]},
    {"id": 62, "name": "Leg Curl (Lying)",                   "primary": "hamstrings", "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "hamstrings", "full"]},
    {"id": 63, "name": "Leg Curl (Seated)",                  "primary": "hamstrings", "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "hamstrings", "full"]},

    # ── GLUTES ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 64, "name": "Hip Thrust (Barbell)",               "primary": "glutes",     "secondary": "hamstrings", "type": "compound",  "equipment": "barbell",    "difficulty": "medium", "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes"]},
    {"id": 65, "name": "Hip Thrust (Smith Machine)",         "primary": "glutes",     "secondary": "hamstrings", "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes", "full"]},
    {"id": 66, "name": "Hip Thrust (Dumbbell)",              "primary": "glutes",     "secondary": "hamstrings", "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes", "full"]},
    {"id": 67, "name": "Lunge (Dumbbell)",                   "primary": "glutes",     "secondary": "quads",      "type": "compound",  "equipment": "dumbbell",   "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes", "full"]},
    {"id": 68, "name": "Lunge (Smith Machine)",              "primary": "glutes",     "secondary": "quads",      "type": "compound",  "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes"]},
    {"id": 69, "name": "Cable Kickback",                     "primary": "glutes",     "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "glutes"]},

    # ── CALVES ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 70, "name": "Calf Raise (Machine)",               "primary": "calves",     "secondary": None,         "type": "isolation", "equipment": "machine",    "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "calves", "full"]},
    {"id": 71, "name": "Calf Raise (Smith Machine)",         "primary": "calves",     "secondary": None,         "type": "isolation", "equipment": "smith",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["legs", "calves", "full"]},

    # ── ABS / CORE ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {"id": 72, "name": "Crunch (Bodyweight)",                "primary": "core",       "secondary": None,         "type": "isolation", "equipment": "bodyweight", "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["core", "full"]},
    {"id": 73, "name": "Crunch (Weighted)",                  "primary": "core",       "secondary": None,         "type": "isolation", "equipment": "bodyweight", "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["core", "full"]},
    {"id": 74, "name": "Cable Crunch",                       "primary": "core",       "secondary": None,         "type": "isolation", "equipment": "cable",      "difficulty": "low",    "min_exp": "beginner",     "knee_safe": True,  "shoulder_safe": True,  "spine_safe": True,  "tags": ["core", "full"]},

]

# ════════════════════════════════════════════════════════════════════
# FILTER LOGIC
# ════════════════════════════════════════════════════════════════════

EXP_ORDER = {"beginner": 0, "intermediate": 1, "advanced": 2}

SESSION_TAG_MAP = {
    # standard splits
    "Full-Body":  "full",
    "Upper":      "upper",
    "Lower":      "legs",
    "Push":       "push",
    "Pull":       "pull",
    "Legs":       "legs",
    # bro-split (Split-4 / 5-day)
    "Chest":      "chest",
    "Back":       "back",
    "Shoulders":  "shoulders",
    "Arms":       "arms",
    "Triceps":    "triceps",
    "Biceps":     "biceps",
    "Quads":      "quads",
    "Hamstrings": "hamstrings",
    "Glutes":     "glutes",
    "Calves":     "calves",
    "Core":       "core",
}

def filter_exercises(session_type, experience, limitations=None):
    if limitations is None:
        limitations = []

    tag = SESSION_TAG_MAP.get(session_type, "full")

    result = []
    for ex in EXERCISES:
        if tag not in ex["tags"]:
            continue
        if EXP_ORDER[ex["min_exp"]] > EXP_ORDER[experience]:
            continue
        if "knee"     in limitations and not ex["knee_safe"]:
            continue
        if "shoulder" in limitations and not ex["shoulder_safe"]:
            continue
        if "back"     in limitations and not ex["spine_safe"]:
            continue
        if "elbow"    in limitations and ex["type"] == "isolation" \
                and ex["primary"] in ("triceps", "biceps"):
            continue
        result.append(ex)
    return result
