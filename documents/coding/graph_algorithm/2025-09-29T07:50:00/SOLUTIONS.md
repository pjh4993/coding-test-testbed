Awesome — here are clean, interview-ready solutions for the 5 graph problems. Each comes with **Idea → Code → Why it works → Complexity**. I’ve avoided recursion where possible (per your preference).

---

# 1) Shortest Path in a Weighted Graph (Dijkstra)

## Idea

Use a **min-heap** keyed by current best distance. Relax outgoing edges; if we find a shorter path to `v`, update `dist[v]` and push `(dist[v], v)`.

## Code

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, s):
    g = defaultdict(list)
    for u, v, w in edges:          # directed weighted
        g[u].append((v, w))

    INF = 10**18
    dist = [INF]*n
    dist[s] = 0
    pq = [(0, s)]                  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue               # stale entry
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

## Why it works

A min-heap always expands the node with the smallest tentative distance. With **nonnegative weights**, the first time a node is popped with `d == dist[u]`, its distance is finalized (no shorter path can be found later).

## Complexity

* Build graph: **O(n + m)**
* Each edge relaxes at most once into a heap push: **O(m log n)**
* Total: **O((n + m) log n)**

---

# 2) Detect Cycle in an Undirected Graph (Union-Find)

## Idea

Treat each edge `(u, v)`. If `find(u) == find(v)`, we’ve connected two nodes already in the same component → **cycle**. Otherwise union them.

## Code

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]  # path halving
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.r[ra] < self.r[rb]:
            self.p[ra] = rb
        elif self.r[ra] > self.r[rb]:
            self.p[rb] = ra
        else:
            self.p[rb] = ra
            self.r[ra] += 1
        return True

def has_cycle_undirected(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):   # union failed => same root => cycle
            return True
    return False
```

## Why it works

In an undirected graph, adding an edge between nodes already connected creates exactly one simple cycle. DSU detects this by root equality.

## Complexity

* Near-constant `find`/`union` (amortized inverse Ackermann).
* For `m` edges: **O(m α(n)) ≈ O(m)**.

---

# 3) Course Schedule (Topological Sort / Kahn’s BFS)

## Idea

Model as a **DAG check**. Compute indegrees; repeatedly remove zero-indegree nodes. If we process all `n` nodes, no cycle → feasible. Otherwise, cycle exists.

## Code

```python
from collections import defaultdict, deque

def can_finish_courses(n, prerequisites):
    g = defaultdict(list)
    indeg = [0]*n
    for a, b in prerequisites:   # to take a, must finish b -> edge b->a
        g[b].append(a)
        indeg[a] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    seen = 0

    while q:
        u = q.popleft()
        seen += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return seen == n
```

## Why it works

In a DAG, some node always has indegree 0. Removing zero-indegree nodes topologically sorts the graph. If a cycle exists, you eventually get stuck with nonzero indegrees.

## Complexity

* Build graph + indegrees: **O(n + m)**
* BFS processing each edge once: **O(n + m)**

---

# 4) Minimum Spanning Tree (Kruskal)

## Idea

Sort edges by weight; scan from lightest to heaviest, union endpoints if they’re in different components. Sum accepted edges’ weights.

## Code

```python
def mst_kruskal(n, edges):  # edges: (u, v, w), undirected
    class UF:
        def __init__(self, n):
            self.p = list(range(n))
            self.r = [0]*n
        def find(self, x):
            while self.p[x] != x:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb: return False
            if self.r[ra] < self.r[rb]:
                self.p[ra] = rb
            elif self.r[ra] > self.r[rb]:
                self.p[rb] = ra
            else:
                self.p[rb] = ra
                self.r[ra] += 1
            return True

    uf = UF(n)
    total = 0
    edges_sorted = sorted(edges, key=lambda x: x[2])
    used = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            total += w
            used += 1
            if used == n-1:
                break
    return total if used == n-1 else None  # None if graph disconnected
```

## Why it works

Kruskal is a classic **cut property** algorithm: for any cut, the lightest crossing edge is safe. DSU ensures we never form a cycle and only connect distinct components.

## Complexity

* Sort edges: **O(m log m)**
* DSU unions: **O(m α(n)) ≈ O(m)**
* Total: **O(m log m)** (dominant term)

---

# 5) Number of Islands (BFS flood-fill, non-recursive)

## Idea

Scan the grid; when you see an unvisited `'1'`, start a **BFS** to mark the whole component as visited. Count how many times you start a BFS.

## Code

```python
from collections import deque

def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    R, C = len(grid), len(grid[0])
    seen = [[False]*C for _ in range(R)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        seen[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc] and grid[nr][nc] == "1":
                    seen[nr][nc] = True
                    q.append((nr, nc))

    cnt = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1" and not seen[r][c]:
                cnt += 1
                bfs(r, c)
    return cnt
```

## Why it works

Each BFS explores exactly one connected 4-directional land component. Counting BFS starts equals the island count.

## Complexity

* Each cell is enqueued/dequeued at most once.
* Time: **O(R·C)**; Space: **O(R·C)** worst-case for queue/visited.

---

If you want, I can bundle these into a **single “cheat sheet” file** (py/markdown) with ultra-compact versions and a few quick tests you can run locally.
