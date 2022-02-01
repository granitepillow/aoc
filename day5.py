class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "%d,%d" %(self.x, self.y)
    x = 0
    y = 0

class vent:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __str__(self):
        s = str(self.start)+ " -> " + str(self.end)
        return s
    start = None
    end = None

class board:
    def __init__(self,x,y):
        self.grid = []
        for i in range(y):
            self.grid.append([0,]*x)
        self.x=x
        self.y=y
    def __str__(self):
        s = ""
        for j in range(self.y):
            for i in range(self.x):
                s+="%02d " % (self.grid[j][i])
            s+="\n"
        s+="\n"
        return s
    def add_vent(self,v):
        if (v.start.x == v.end.x):
            s = min(v.start.y, v.end.y)
            e = max(v.start.y, v.end.y)
            for i in range(s, e+1):
                self.grid[i][v.start.x] += 1
                if self.grid[i][v.start.x] == 2:
                    self.count += 1
        elif(v.start.y == v.end.y):
            s = min(v.start.x, v.end.x)
            e = max(v.start.x, v.end.x)
            for i in range(s, e+1):
                self.grid[v.start.y][i] += 1
                if self.grid[v.start.y][i] == 2:
                    self.count += 1
        else:
            print v
            xinc = 1
            yinc = 1

            sv = v.start
            ev = v.end
            if sv.x>ev.x:
                xinc = -1
            if sv.y>ev.y:
                yinc = -1
            for i in range(abs(ev.x-sv.x) + 1):
                print "test %d %d %d %d %d %d %d %d %d %d %d" % (sv.x, sv.y, ev.x, ev.y, i, sv.x+i*xinc, sv.y+i*yinc, self.x, self.y, xinc, yinc)
                self.grid[sv.y+i*yinc][sv.x+i*xinc] += 1
                if self.grid[sv.y+i*yinc][sv.x+i*xinc] == 2:
                    self.count += 1


    grid = None
    x = 0
    y = 0
    count = 0



def get_vent(inp):
    v = inp.split(" -> ")
    
    coords = []
    for c in v:
        cs = c.split(",")
        
        if len(cs) != 2:
            continue
        co = coord(int(cs[0]), int(cs[1]))
        coords.append(co)
    if len(coords) != 2:
        return None
    return vent(coords[0], coords[1])

    

vents = []
with open("input5.txt") as f:
    l=f.readline().strip()

    while l:
        v = get_vent(l)
        if v:
            vents.append(v)
        l=f.readline().strip()

maxx = 0
maxy = 0
for v in vents:
    if v.start.x > maxx:
        maxx = v.start.x
    if v.end.x > maxx:
        maxx = v.end.x

    if v.start.y > maxy:
        maxy = v.start.y
    if v.end.y > maxy:
        maxy = v.end.y

b = board(maxx+1, maxy+1)

print b
for v in vents:
    b.add_vent(v)
    #print "~~~"
    #print v
    #print b
print b.count

