NAME = 0
EQUIPMENT = 1
VARIATIONS = 2
POSITION = 3
TARGET = 4
TIME = 5
NOTES = 6

# Equipment
NONE = 0
WEIGHTS = 1
BANDS = 2
PULL_UP_BAR = 3

# Position
STANDING = 0
SITTING = 1
LAYING_FRONT = 2
LAYING_BACK =3

# Target
# UPPER_ABS
# LOWER_ABS
# SIDE_ABS
# BACK
# BICEPS
# TRICEPS
# SHOULDERS
# PECS

# Time
FULL = 0
HALF = 1


arms = [{NAME: "Push ups", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Triangle pushups", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "High <-> low plank", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "High plank shoulder tap", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Dips", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Inchworms", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Pulse Backs", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Gorilla pushups", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Plank Hops", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Star pushups", EQUIPMENT:NONE, VARIATIONS:[]},
{NAME: "Knee pushup + reach back to toe tap", EQUIPMENT:NONE, VARIATIONS:[]},

{NAME: "Bicep curls", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"," + lunges"," + wall sit"]},
{NAME: "Arm circles", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"," + lunges"," + wall sit"]},
{NAME: "Static hold", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"," + lunges"," + wall sit"]},
{NAME: "Shoulder press", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"," + lunges"," + wall sit"," + burpie"]},
{NAME: "Rows/lawnmowers", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Arm flys front and side", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Tricep kickbacks", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Back scratcher", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Weighted Rainbow", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Chest flys", EQUIPMENT:WEIGHTS, VARIATIONS:[]},
{NAME: "Deadlift", EQUIPMENT:WEIGHTS, VARIATIONS:[]},

# {NAME: "Nutcrackers", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"]},
# {NAME: "Chest flys", EQUIPMENT:WEIGHTS, VARIATIONS:[" + squats"]},
]


import random
new_set = random.sample(range(0, len(arms)), 5)

for exercise in new_set:
    print(arms[exercise][NAME])



