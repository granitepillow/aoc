class Fish:
    def __init__(self, start):
        self.timer = start
    def __str__(self):
        return str(self.timer)
    timer = 10

class School:
    def __init__(self):
        self.fishes = []
    def __str__(self):
        s = ""
        for f in self.fishes:
            s += str(f) + ","

        return s + "\n"
    def add_fish(self,timer):
        self.fishcounts[timer] += 1
        print self.fishcounts
    def advance_day(self, day):
        tmp_new = self.fishcounts[day%7] - self.new_1
        self.fishcounts[(day+2) %7] += tmp_new
        self.new_1 = self.new_2
        self.new_2 = tmp_new
    def total(self):
        sm = 0
        for f in self.fishcounts:
            sm+=f
        return sm

    fishcounts=[0,]*7
    new_1 = 0
    new_2 = 0


s = School()
with open("input6.txt") as f:
    l=f.readline().strip().split(",")
    for e in l:
        s.add_fish(int(e))

for i in range(256):
    print "after %d days, %d (%d %d)" %(i, s.total(), s.new_1, s.new_2)
    s.advance_day(i)

print s.total()

