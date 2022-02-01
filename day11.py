class Octopus:
    def __init__(self, v):
        self.val = v
        self.flashed = False

    def flashready(self):
        return self.val >= 10 and not self.flashed

class Grid:
    def __init__(self, grid):
        self._grid = []
        for j in grid:
            row = []
            for i in j:
                row.append(Octopus(i))
            self._grid.append(row)
        self.X = len(grid[0])
        self.Y = len(grid)
    def __str__(self):
        s = ""
        for j in self._grid:
            for i in j:
                if i.val >= 10:
                    s+= "#"
                elif i.val == 0:
                    s += "."
                else:
                    s += "%d" % (i.val)
            s += "\n"
        s += "\n"
        return s
    def _flash(self, x, y):
        left = x > 0
        right = x < self.X-1
        up = y > 0
        down = y < self.Y-1
        if left:
            self._grid[y][x-1].val += 1
            
        if right:
            self._grid[y][x+1].val += 1
            
        if up:
            self._grid[y-1][x].val += 1
            
        if down:
            self._grid[y+1][x].val += 1
            
        if down and right:
            self._grid[y+1][x+1].val += 1
            
        if down and left:
            self._grid[y+1][x-1].val += 1
            
        if up and right:
            self._grid[y-1][x+1].val += 1
            
        if up and left:
            self._grid[y-1][x-1].val += 1
        self._grid[y][x].flashed = True
            

    def step(self):
        done = True
        flashes = 0
        for j in range(self.Y):
                for i in range(self.X):
                    self._grid[j][i].val += 1
                    if self._grid[j][i].val >= 10:
                        done = False
        while not done:
            done = True
            for j in range(self.Y):
                for i in range(self.X):
                    if self._grid[j][i].flashready():
                        self._flash(i, j)
                        flashes += 1
                        done = False

        for j in range(self.Y):
            for i in range(self.X):
                if self._grid[j][i].flashed:
                    self._grid[j][i].flashed = False
                    self._grid[j][i].val = 0

        return flashes
    def sync(self):
        for j in self._grid:
            for i in j:
                if i.val != 0:
                    return False
        return True



grid = []
with open("input11.txt") as f:
    l=f.readline().strip()
    while l:
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row)
        l=f.readline().strip()
g = Grid(grid)
flashes = 0
for i in range(1000):
    if i < 5 or (i > 192 and i < 196):
        print(g)
    flashes += g.step()
    if g.sync():
        print(g)
        print("sync" + str(i))
        break

print (flashes)