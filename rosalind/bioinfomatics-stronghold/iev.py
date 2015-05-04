#!/usr/bin/env python3

couples = [16088, 16352, 18564, 18579, 16144, 16494]
rates = [2.0, 2.0, 2.0, 1.5, 1.0, 0]

count = 0
for i in range(0, 6):
    count += couples[i] * rates[i]

print(count)
