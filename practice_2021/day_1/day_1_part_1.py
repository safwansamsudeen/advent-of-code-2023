prev_number = 0
increased_counter = -1
with open("input.txt") as file:
    for n in file.readlines():
        print(prev_number, n, increased_counter)
        if int(n) > prev_number:
            increased_counter += 1
        prev_number = int(n)
print(increased_counter)
