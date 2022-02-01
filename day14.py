rules = {}
inp = None
with open("input14.txt") as f:
    l=f.readline().strip()
    inp = l
    l=f.readline().strip() #blank line
    l=f.readline().strip()
    while l:
        key = l[:2]
        change = key[0] + l[6]
        rules[key] = change
        l=f.readline().strip()

paircounts = {}
for i in range(len(inp)):
    c = inp[i:i+2]
    if len(c.strip()) < 2:
        break
    if c not in paircounts:
        paircounts[c] = 0
    paircounts[c] += 1

def update_paircounts(pcs, rules):
    new_pcs = {}
    for pc in pcs:
        if pc in rules:
            if pc not in new_pcs:
                new_pcs[pc] = 0
            new_pcs[pc] -= pcs[pc]
            change1 = rules[pc]
            change2 = change1[-1] + pc[-1]
            if change1 not in new_pcs:
                new_pcs[change1] = 0
            if change2 not in new_pcs:
                new_pcs[change2] = 0
            new_pcs[change1] += pcs[pc]
            new_pcs[change2] += pcs[pc]
    for pc in new_pcs:
        if pc not in pcs:
            pcs[pc] = 0
        pcs[pc] += new_pcs[pc]
    return pcs


# def step(inp, rules):
#     outp = ""
#     for i in range(len(inp)):
#         c = inp[i:i+2]
        
#         if c not in rules:
#             outp += inp[i]
#             continue
        
#         outp += rules[c]
#         i+=2
#     return outp

# def most_least_diff(inp):
#     counts = {}
#     for c in inp:
#         if c not in counts:
#             counts[c] = 0
#         counts[c]+=1
#     l = []
#     reverse = {}
#     for c in counts:
#         l.append(counts[c])
#         reverse[counts[c]] = c
#     l.sort()
#     print(reverse)
#     print(counts)
#     most = reverse[l[0]]
#     least = reverse[l[-1]]
#     diff = l[-1]-l[0]
#     return diff

def calc_diff(last_letter, pcs):
    letter_counts = {}
    counts = []
    letter_counts[last_letter] = 1
    for pc in pcs:
        l = pc[0]    
        if l not in letter_counts:
            letter_counts[l] = 0
        letter_counts[l] += pcs[pc]

    for lc in letter_counts:
        counts.append(letter_counts[lc])
    # print(letter_counts)
    counts.sort()
    return counts[-1]-counts[0]


pcs = paircounts
for i in range(40):
    # print(pcs)
    # print(calc_diff(inp[-1], pcs))
    # print("~~~~")
    pcs = update_paircounts(pcs, rules)


print(calc_diff(inp[-1], pcs))


