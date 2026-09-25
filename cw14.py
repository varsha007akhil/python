
import random
import math
names = input("Enter names of guests list: ")
invited = []
for x in names.split(","):
    x = x.strip()
    if x not in invited:
        invited.append(x)
print("Invited guests:", invited)
random_name = random.choice(invited)
print("Randomly selected guest:", random_name)
reversed_name = random_name[::-1]
print("Reversed random name:", reversed_name)
unique_count = len(invited)
sqrt_value = math.sqrt(unique_count)
rounded_sqrt = round(sqrt_value)
print("Total number of unique names:", unique_count)
print("Rounded sqrt:", rounded_sqrt)