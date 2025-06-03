p = []
n = 6
counter = 0;
def pt(i):
    global counter
    if i > n:
        print(p)
        counter += 1
        return
    for pp in p:
        pp.append(i)
        pt(i+1)
        pp.pop()
    p.append([i])
    pt(i+1)
    p.pop()

pt(1)
print(counter)