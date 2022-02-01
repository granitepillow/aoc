

class Grid:
    def __init__(self, x, y):
        self._grid = []
        for j in range(y):
            row = []
            for i in range(x):
                row.append(0)
            self._grid.append(row)
        
        self.X = x
        self.Y = y

    def __str__(self):
        s = ""
        for j in range(self.Y):
            for i in range(self.X):
                if self._grid[j][i]:
                    s+="#"
                else:
                    s+="."
            s +="\n"
        return s

    def fold_vert_crease(self, x):
        new_grid = []
        new_x = (self.X +1)/2 -1
        new_x = int(min(new_x, self.X - x -1))
            
        for j in range(self.Y):
            row = [0] * new_x
            for i in range(new_x):
                
                row[-1-i] = self._grid[j][x-1-i] | self._grid[j][x+1+i]
            new_grid.append(row)
        self.X = new_x
        self._grid = new_grid

    def fold_hori_crease(self, y):
        new_grid = []
        new_y = (self.Y +1)/2 -1
        new_y = int(min(new_y, self.Y - y -1))
            
        for j in range(new_y):
            row = [0] * self.X
            for i in range(self.X):
                
                row[i] = self._grid[y-1-j][i] | self._grid[y+1+j][i]
            new_grid.insert(0, row)
        self.Y = new_y
        self._grid = new_grid

    def add_coord(self,c):
        self._grid[c[1]][c[0]] = 1
    def count(self):
        c = 0
        for j in range(self.Y):
            for i in range(self.X):
                if self._grid[j][i]:
                    c+=1
        return c





coords = []
folds = []
maxx=0
maxy=0
with open("input13.txt") as f:
    l=f.readline()
    while l:
        l = l.strip()

        if l:
            if l[0] == "f":
                fold = l.split("=")
                folds.append([fold[0][-1], int(fold[1])])
            else:
                c = l.split(',')
                c[0] = int(c[0])
                c[1] = int(c[1])
                if c[0] > maxx:
                    maxx = c[0]
                if c[1] > maxy:
                    maxy = c[1]
                coords.append(c)
        l=f.readline()


g = Grid(maxx+1, maxy+1)
for c in coords:
    g.add_coord(c)

for f in folds:
    if f[0] == "x":
        g.fold_vert_crease(f[1])
        
    else:
        g.fold_hori_crease(f[1])
    print(g)
    print(g.count())


