class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.nodes = []
        self.x = x
        self.y = y
    def __lt__(self, b):
        return self.val < b.val
    def __str__(self):
        s = "%d,%d = %d" %(self.x, self.y, self.val)
        return s

class Grid:
    def __init__(self, grid):
        self.grid = []
        self.mp = []
        self.X = len(grid[0])
        self.Y = len(grid)
        self.MX = 5 * self.X
        self.MY = 5 * self.Y
        for j in range(self.Y):
            row = []
            for i in range(self.X):
                row.append(grid[j][i])
            self.grid.append(row)
        for j in range(self.MY):
            mrow = []
            for i in range(self.MX):
                mrow.append(Node(-1, i, j))
            self.mp.append(mrow)
        
        

    def __str__(self):
        NUM_CHARS = 1
        s = ""
        for j in self.mp:
            for i in j:
                if i.val == -1:
                    s += "."*NUM_CHARS
                else:
                    s2=str(i.val)
                    while len(s2) < NUM_CHARS:
                        s2 = "0"+s2
                    if len(s2) > NUM_CHARS:
                        s2 = s2[0:NUM_CHARS]
                    s += s2
                if NUM_CHARS > 1:
                    s += " "

            s+="\n"
        return s

    def _append_node(self, x, y, current_cost, next_nodes):
        if x < 0 or y < 0 or x >= self.MX or y >= self.MY:
            return
        node = self.mp[y][x]
        if node.val >= 0: #visited
            return
        next_nodes.append(node)
        gx = x % self.X
        gy = y % self.Y
        add_cost = (self.grid[gy][gx] + int(x/self.X) + int(y/self.Y))
        while add_cost > 9: # not quite modulo operation
            add_cost -= 9

        node.val = add_cost + current_cost
 
    def traverse(self):
        self.mp[0][0].val = 0
        next_nodes = []
        node = self.mp[0][0]
        while True:
            #print(node)
            print(self)
            # for n in next_nodes:
            #     print(n)
            x = node.x
            y = node.y
            self._append_node(x-1, y, node.val, next_nodes)
            self._append_node(x+1, y, node.val, next_nodes)
            self._append_node(x, y-1, node.val, next_nodes)
            self._append_node(x, y+1, node.val, next_nodes)

            next_nodes.sort()
            node = next_nodes[0]
            next_nodes = next_nodes[1:]
            if node.x == self.MX-1 and node.y == self.MY-1:
                return node.val
         








grid = []
with open("input15.txt") as f:
    l=f.readline().strip()
    while l:
        
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row)
        l=f.readline().strip()

# print(grid)

g = Grid(grid)
print(g.traverse())