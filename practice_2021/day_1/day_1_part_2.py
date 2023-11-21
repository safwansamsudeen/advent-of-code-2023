from collections import deque
current_window = deque(maxlen=3)
prev_sum = 0
counter = -3

with open("day_1_input.txt") as f:
    for n in f.readlines():
        current_window.append(int(n))
        s = sum(current_window)
        if s > prev_sum:
            counter += 1
        prev_sum = s
print(counter)
