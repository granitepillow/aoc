

op = ("{", "[", "(", "<")
cl = ("}", "]", ")", ">")
points = {"{":3 , "(":1, "[":2, "<":4}
scores = []
with open("input10.txt") as f:
    l=f.readline().strip()
    while l:
        total = 0
        stack = []
        illegal = False
        for c in l:
            if c in op:
                stack.append(c)
            elif c in cl:
                test = stack.pop()
                if abs(ord(c)-ord(test)) > 2:
                    print("illegal")
                    illegal = True
                    break
            else:
                print("super illegal")
                illegal = True
                break
        if not illegal:
            while len(stack) > 0:
                c = stack.pop()
                print(c)
                total = (total*5) + points[c]
                print(total)
            scores.append(total)
        print("~~~")
        l=f.readline().strip()
print(scores)
scores.sort()
print(scores[int(len(scores)/2)])