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



nodes = []
class Node:
    def __init__(self, name):
        self.big = (name[0] >= 'A' and name[0] <= 'Z')
        self.name = name
        self.conns = set()
        self.visieted = False
    def add_conn(self,conn):
        self.conns.add(conn)

class Map:
    def __init__(self):
        self.nodes = {}
    def __str__(self):
        s = ""
        for i in self.nodes:
            s += str(i) + ": "
            for c in self.nodes[i].conns:
                s += c.name + ", "
            s += "\n"
        return s

    def add_node(self, node):
        self.nodes[node.name] = node
    def add_conn(self, aname, bname):
        if aname not in self.nodes:
            a = Node(aname)
            self.add_node(a)
        if bname not in self.nodes:
            b = Node(bname)
            self.add_node(b)
        self.nodes[aname].add_conn(self.nodes[bname])
        self.nodes[bname].add_conn(self.nodes[aname])

    def _count_instances(self, chain, n):
        count = 0
        for c in chain:
            if n.name == c:
                count += 1
        return count

    def routesfrom(self, chain, n, allowed):
        if n.name == "start":
            return 1

        routes = 0
        new_chain = []
        for c in chain:
            new_chain.append(c)
        new_chain.append(n.name)

        for c in n.conns:
            if c.name == "end":
                continue
            if (not c.big and c.name in new_chain):
                if allowed:
                    routes += self.routesfrom(new_chain, c, False)
                continue
            else:
                routes += self.routesfrom(new_chain, c, allowed)
        return routes

    def traverse(self, nn="end"):
        n = self.nodes[nn]
        chain = [nn,]
        routes = 0
        for c in n.conns:
            routes += self.routesfrom(chain, c, True)
        return routes




m = Map()
with open("input12.txt") as f:
    l=f.readline().strip()
    while l:
        c = l.split('-')
        m.add_conn(c[0], c[1])
        l=f.readline().strip()
print(m)

print(m.traverse())
