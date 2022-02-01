class cell:
    def __init__(self,v):
        self.mrk = False
        self.val = v
    def mark(self):
        self.mrk=True
    
    mrk = False
    val = -1

class board:
    def __init__(self):
        self.rows = []
    def __str__(self):
        s = ""
        for r in self.rows:
            for el in r:
                s += "%02d" %(el.val)
                if el.mrk:
                    s+="#"
                else:
                    s+=" "
                s+=" "
            s+= "\n"
        s+= "\n"
        return s

    def check_winner(self):
        if not self.comp:
            return False
        sm = 0
        cols = [True,]*len(self.rows[0])
        for r in self.rows:
            good = True
            for i,e in enumerate(r):
                if not e.mrk:
                    good = False
                    cols[i]=False
                    sm += e.val
            if good:
                self.win = True
        for i,c in enumerate(cols):
            if c or self.win:
                self.win = True
                return sm
        return False

    def mark(self, v):
        for row in self.rows:
            for el in row:
                if el.val == v:
                    el.mark()
    def add_cell(self, c):
        if len(self.rows) == 0 or len(self.rows[-1]) == 5:
            if len(self.rows) == 5:
                self.comp = True
                return False

            self.rows.append([])
        self.rows[-1].append(c)

    def complete(self):
        if len(self.rows) == 5 and len(self.rows[-1]) == 5:
            self.comp = True
            return True
        return False
    rows = []
    comp = False
    win = False



with open("input4.txt") as f:
    l=f.readline().strip()
    calls = l.split(",")
    for i in range(len(calls)):
        calls[i] = int(calls[i])
    boards = []
    b = board()
    l=f.readline()
    while l:
        if l.strip():
            line = l.strip().split()
            for i in range(len(line)):
                b.add_cell(cell(int(line[i].strip())))
            if b.complete():
                boards.append(b)
                b = board()
        l=f.readline()

win = False
for c in calls:
    for b in boards:
        if b.win:
            continue
        b.mark(c)
        s = b.check_winner()
        if s:
            print c
            print b
            print s*c
            print "~~~"
            continue
