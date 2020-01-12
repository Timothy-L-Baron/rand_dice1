"""Make a random number generator for D&D statistics that generates 4d6 'take the best 3' results"""
import random
count = 0

#function to find the minimum roll
def find_min(v1, v2, v3, v4):
    scores = []
    scores.append(v1)
    scores.append(v2)
    scores.append(v3)
    scores.append(v4)
    min_roll = min(scores)
    return min_roll

for score in range(6):
    value1 = random.randint(1, 6)
    value2 = random.randint(1, 6)
    value3 = random.randint(1, 6)
    value4 = random.randint(1, 6)
    min_roll = find_min(value1, value2, value3, value4)
    roll_total = value1 + value2 + value3 + value4 - min_roll
    if count == 0:
        print('S: {}'.format(roll_total))
    if count == 1:
        print('D: {}'.format(roll_total))
    if count == 2:
        print('C: {}'.format(roll_total))
    if count == 3:
        print('I: {}'.format(roll_total))
    if count == 4:
        print('W: {}'.format(roll_total))
    if count == 5:
        print('C: {}'.format(roll_total))
    count = count + 1
