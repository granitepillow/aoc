


def get_most(rs, pos):
    cnt = 0
    tot = 0
    for r in rs:
        if not r["oko"]:
            continue
        tot +=1
        if r["v"] & (1<<pos):
            cnt+=1

    if cnt >= tot / 2:
        return 1, tot
    return 0, tot

def get_least(rs, pos):
    cnt = 0
    tot = 0
    for r in rs:
        if not r["okc"]:
            continue
        tot +=1
        if r["v"] & (1<<pos):
            cnt+=1

    if cnt <= tot / 2:
        return 1, tot
    return 0, tot

def get_o2_co2(rs, bitlen):
    o2 = 0
    co2 = 0
    for i in range(bitlen):
        test = bitlen-1-i

        m, tot = get_most(rs, test)
        print rs
        print m<<test
        if tot == 1:
            break
        for r in rs:
            if not (r["v"] & (m<<test)):
                r["oko"] = False
    for r in rs:
        if r["oko"]:
            o2 = r["v"]
    for i in range(bitlen):
        test = bitlen-1-i

        m, tot = get_least(rs, test)
        if tot == 1:
            break
        for r in rs:
            if not (r["v"] & (m<<test)):
                r["okc"] = False
    for r in rs:
        if r["okc"]:
            co2 = r["v"]
    return o2, co2



rows = []

def get_mid(rows, bitlen, least = False):
    rows.sort()
    start = 0
    end = len(rows)
    for i in range(bitlen):
        print rows[start:end]
        if len(rows[start:end]) <= 2:
            if least:
                return rows[start]
            return rows[end-1]
        testbit = 1 << bitlen-1-i
        mid = (end-start) / 2 + start
        keep = rows[mid] & testbit
        if least:
            keep ^= testbit
        if keep == 0:
            for i in range(start,end):
                if rows[i] & testbit:
                    end = i
                    break
        else:
            for i in range(start,end):
                if rows[i] & testbit:
                    start = i
                    break
                    

with open("input3.txt") as f:
    l=f.readline()
    i = 0
    bitlen = len(l.strip())
    while l:
        rows.append(int(l.strip(),2))
        i+=1
        l=f.readline()

    o2 = get_mid(rows, bitlen)
    

    co2 = get_mid(rows, bitlen, True)
    
    print o2 * co2
            


#print get_o2_co2(rows, bitlen)



# counts = [0,]*len(rows[0])

# for r in rows:
#     val = int(r,2)
#     for i in range(len(counts)):
#         counts[-1-i] += val & 1
#         val>>=1
# mult = 2**(len(counts)-1)
# print len(counts)
# gamma = 0
# epsilon = 0
# for c in counts:
#     if c > len(rows)/2:
#         gamma += mult
#     else:
#         epsilon += mult
#     mult >>= 1
# print bin(gamma)
# print bin(epsilon)
# print gamma*epsilon

# mostcommon = [0,]*len(counts)
# for i in range(len(counts)):
#     if counts[i] > len(rows)/2:
#         mostcommon[i] = 1

# for r in rows:


# def get_counts(somerows):
#     counts = [0,]*len(rows[0])
#     for r in somerows:
#         val = int(r,2)
#         for i in range(len(counts)):
#             counts[-1-i] += val & 1
#             val>>=1
#     for c in counts:
#         if c > len(somerows)/2:

#     most = []
#     least = []
#     return most, least