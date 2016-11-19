def zombieCluster(zombies):
    zombies = [list(z) for z in zombies]
    n = len(zombies)
    visited = set()
    cluster = 0
    while len(visited) < n:
        for i in range(0, n):
            if i not in visited:
                break
        dfs(i, zombies, visited)
        cluster += 1
    return cluster


def dfs(z, zombies, visited):
    n = len(zombies)
    visited.add(z)
    if len(visited) == len(zombies):
        return
    else:
        for i in range(0, n):
            if i not in visited:
                if zombies[z][i] == '1':
                    dfs(i, zombies, visited)
        return

zombies=['1100','1110','0110','0001']
print(zombieCluster(zombies))