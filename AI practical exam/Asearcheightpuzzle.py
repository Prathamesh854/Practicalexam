import heapq
def manhattan_distance(p, g):
    return sum(abs(i // 3 - p.index(g[i]) // 3) + abs(i % 3 - p.index(g[i]) % 3) for i in range(9) if p[i] != 0)
def is_solvable(p, g):
    return sum(sum(p[i] > p[j] for j in range(i + 1, len(p)) if p[j] != 0) for i in range(len(p) - 1)) % 2 == 0
def solve_puzzle(p, g):
    if not is_solvable(p, g):
        return [], []
    h, v = [], set()
    heapq.heappush(h, (0, p, []))
    while h:
        c, c_p, pth = heapq.heappop(h)
        if c_p == g:
            return len(pth), pth
        z = c_p.index(0)
        x, y = z // 3, z % 3
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < 3 and 0 <= y2 < 3:
                n_p = list(c_p)
                nz = x2 * 3 + y2
                n_p[z], n_p[nz] = n_p[nz], n_p[z]
                n_pth = pth + [(x, y, x2, y2)]
                n_c = c + 1
                if tuple(n_p) not in v:
                    v.add(tuple(n_p))
                    heapq.heappush(h, (n_c, n_p, n_pth))
    return [], []
if __name__ == '__main__':
    p, g = [1, 2, 3, 0, 4, 6, 7, 5, 8], [1, 2, 3, 4, 5, 6, 7, 8, 0]
    c, pth = solve_puzzle(p, g)
    if c:
        print('Found solution with cost', c)
        print('\nStart State:')
        for i in range(3):
            print(p[i * 3:i * 3 + 3])
        for s, m in enumerate(pth, start=1):
            x1, y1, x2, y2 = m
            p[x1 * 3 + y1], p[x2 * 3 + y2] = p[x2 * 3 + y2], p[x1 * 3 + y1]
            print(f'\nStep {s}:')
            for i in range(3):
                print(p[i * 3:i * 3 + 3])
    else:
        print('No solution found')