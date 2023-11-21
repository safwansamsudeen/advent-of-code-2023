def forward(n):
    pos[0] += n
def up(n):
    pos[1] -= n
def down(n):
    pos[1] += n

d = {'forward': forward, 'up': up, 'down': down}
pos = [0, 0]
with open('day_2_input.txt') as f:
    for stmt in f.readlines():
        cmd, n = stmt.split()
        d[cmd](int(n))
print(pos[0] * pos[1])
