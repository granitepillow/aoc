import math


class Digit:
    def __init__(self):
        self.val = -1
        self._segs = []

    def num_segs(self):
        return len(self._segs)
    def segs(self):
        return set(self._segs)
    def append_seg(self, s):
        self._segs.append(s)

class DigitSet:
    def __init__(self, ds):
        self.known_digs = {}
        unknown_digs = []
        for d in ds:
            dig = Digit()
            for s in d:
                dig.append_seg(s)
            if dig.num_segs() == 2:
                dig.val = 1
            elif dig.num_segs() == 3:
                dig.val = 7
            elif dig.num_segs() == 4:
                dig.val = 4
            elif dig.num_segs() == 7:
                dig.val = 8
            else:
                unknown_digs.append(dig)
            if dig.val != -1:
                self.known_digs[dig.val] = dig
        for d in unknown_digs:
            if d.num_segs() == 6:
                print (self.known_digs[4].segs())
                print (d.segs())
                if self.known_digs[4].segs().issubset(d.segs()):
                    d.val = 9
                elif self.known_digs[7].segs().issubset(d.segs()):
                    d.val = 0
                else:
                    d.val = 6
                self.known_digs[d.val] = d
            elif self.known_digs[7].segs().issubset(d.segs()):
                d.val = 3
                self.known_digs[d.val] = d
        for d in unknown_digs:
            if d.val == -1:
                if d.segs().issubset(self.known_digs[9].segs()):
                    d.val = 5
                else:
                    d.val = 2
                self.known_digs[d.val] = d
        
        if len(self.known_digs) != 10:
            print ("AHH!")
            print (self.known_digs)
            
        unknown_digs = []

    def get_digit(self, segs):
        for k in self.known_digs:
            print(len(segs))
    
            if len(segs) != self.known_digs[k].num_segs():
                continue
            match = True
            print(segs)
            print(self.known_digs[k].segs())
            if not set(segs).issubset(self.known_digs[k].segs()):
                    match = False
            if match:
                return self.known_digs[k].val
        return None

        











lines = []
with open("input8.txt") as f:
    l=f.readline().strip()
    while l:
        row = l.split("|")
        line = []
        for p in row:
            line.append(p.split())
        lines.append(line)
        l=f.readline().strip()

total = 0
for l in lines:
    dset = DigitSet(l[0])
    
    outp = 0 
    for e in l[1]:
        outp = outp*10 + dset.get_digit(e.strip())
    total += outp
print (total)
