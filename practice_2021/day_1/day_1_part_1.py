prev_number = 0
increased_counter = -1
with open("day_1_input.txt") as file:
    for n in file.readlines():
        n = int(n)
        if n > prev_number:
            increased_counter += 1
        prev_number = n
print(increased_counter)
