import math
crabs = []
with open("input7.txt") as f:
    l=f.readline().strip().split(",")
    for e in l:
        crabs.append(int(e))

m = min(crabs)
ma = max(crabs)

diff = -1
for i in range(m, ma+1):
    fuel = 0
    for c in crabs:
        num = abs(i-c)
        fuel+=(num+1)/2.0 *num
    if fuel < diff or diff == -1:
        diff = fuel

print diff

