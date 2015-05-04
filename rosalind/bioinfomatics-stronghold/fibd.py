#!/usr/bin/env python3

after_month = 87
live_month = 17

rabbits = [0 for i in range(0, live_month)]
rabbits[0] = 1

for d in range(1, after_month):
    new_rabbits = [0 for i in range(0, live_month)]
    for r in range(0, live_month):
        if r == 0:
            new_rabbits[r] = sum(rabbits[1:])
        else:
            new_rabbits[r] = rabbits[r-1]

    rabbits = new_rabbits

print(sum(rabbits))
