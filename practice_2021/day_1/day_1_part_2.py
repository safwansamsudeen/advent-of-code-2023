from collections import deque
current_window = deque(maxlen=3)
prev_sum = 0
counter = -3

with open("input.txt") as f:
    for n in f.readlines():
        print(current_window)
        current_window.append(int(n))
        if sum(current_window) > prev_sum:
            counter += 1
        prev_sum = sum(current_window)
print(counter)
