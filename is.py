from random import randrange

g = [(u,v) for u in range(6) for v in range(u+1,6) if randrange(2)]

used = [False for i in range(6)]
vertexes = []

def solve(g):
    if all(used):
        print(vertexes)
        return
    p1 = used.index(False)
    used[p1] = True
    solve(g)
    used[p1] = False
    used[p1] = True
    for e in g:
        if p1 in e:
            used[e[0]] = True
            used[e[1]] = True
    vertexes.append(p1)
    solve(g)
    vertexes.pop()
    for e in g:
        if p1 in e:
            used[e[0]] = False
            used[e[1]] = False
    used[p1] = False

print(g)
solve(g)