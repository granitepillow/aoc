cmds = []
with open("input2.txt") as f:
    l=f.readline()
    while l:
        cmds.append(l.strip())
        l=f.readline()

hor = 0
ver = 0
aim = 0

for c in cmds:
    a = c.split(' ')
    if len(a) < 2:
        print "error"
        continue
    d = a[0]
    s = int(a[1])
    if d == "forward":
        hor += s
        ver += (aim*s)
    elif d == "up":
        #ver -= s
        aim -= s
    elif d == "down":
        #ver += s
        aim += s
    else:
        print d

print "%d %d %d" %(hor, aim, ver)
print hor*ver
