class Point:
    def __init__(self,x,y, val):
        self.x = x
        self.y = y
        self.val = val
        self.basin = None

class Grid:
    def __init__(self, grid):
        self._grid = []
        self.X = len(grid[0])
        self.Y = len(grid)
        self.lows = []
        self.basins = []
        for y, row in enumerate(grid):
            irow = []
            for x,e in enumerate(row):
                irow.append(Point(x,y,e))
            self._grid.append(irow)
        for y, row in enumerate(self._grid):
            for x, e in enumerate(row):
                if self.test_low(x, y):
                    self.add_low(x,y,e.val)
        for i, l in enumerate(self.lows):
            self.basins.append(self.get_basin(l,i))

    def test_low(self, x, y):
        e = self._grid[y][x]
        if x > 0:
            if self._grid[y][x-1].val <= e.val:
                return False
        if x < self.X-1:
            if self._grid[y][x+1].val <= e.val:
                return False
        if y > 0:
            if self._grid[y-1][x].val <= e.val:
                return False
        if y < self.Y-1:
            if self._grid[y+1][x].val <= e.val:
                return False     
        return True

    def add_low(self, x,y,v):
        self.lows.append(Point(x,y,v))

    def _test_basin(self, size, x, y, i):
        print("test %d %d %i" % (x,y,i))
        if self._grid[y][x].val == 9 or self._grid[y][x].basin:
            return 0
        size = 1
        self._grid[y][x].basin = i+1
        if x > 0:
            size += self._test_basin(size, x-1, y, i)
        if x < self.X-1:
            size += self._test_basin(size, x+1, y, i)
        if y > 0:
            size += self._test_basin(size, x, y-1, i)
        if y < self.Y-1:
            size += self._test_basin(size, x, y+1, i)
        return size
    
    def get_basin(self,low, i):
        size = self._test_basin(0, low.x, low.y, i)
        return size
            







grid = []
with open("input9.txt") as f:
    l=f.readline().strip()
    while l:
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row)
        l=f.readline().strip()

G = Grid(grid)

print(G.basins)
G.basins.sort()
print(G.basins[-1]*G.basins[-2]*G.basins[-3])
