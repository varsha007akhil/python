import random
import math
names = input("Enter customer names: ")
participants = []
for name in names.split(","):
    name = name.strip()
    if name not in participants:
        participants.append(name)
random.shuffle(participants)
winners = random.sample(participants, 2)
print("Unique participants:", participants)
print("Winner 1:", winners[0][::-1])
print("Winner 2:", winners[1][::-1])
total = len(participants)
print("Total number of unique participants:", total)
sqrt_value = math.sqrt(total)
print("Rounded square root:", round(sqrt_value))