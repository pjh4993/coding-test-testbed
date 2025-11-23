Perfect — here are **5 graph algorithm problems** in the style you requested, with problem statements, examples, hints, and a difficulty grade.

---

### 1. Shortest Path in a Weighted Graph (Dijkstra)

**Problem:**
You are given a directed weighted graph with `n` nodes. Find the shortest distance from a given source node `s` to every other node.

**Example:**

```
Input: n = 5, edges = [(0,1,2),(0,2,4),(1,2,1),(1,3,7),(2,4,3)], s = 0
Output: [0,2,3,9,6]
Explanation: Shortest paths are
0→1 (2), 0→1→2 (3), 0→1→3 (9), 0→1→2→4 (6)
```

**Hint:**
Use a **priority queue (min-heap)** to always expand the nearest unvisited node.

**Grade:** Medium

---

### 2. Detect Cycle in an Undirected Graph

**Problem:**
Given an undirected graph with `n` nodes, determine if the graph contains a cycle.

**Example:**

```
Input: n = 4, edges = [(0,1),(1,2),(2,0),(2,3)]
Output: True
Explanation: 0→1→2→0 forms a cycle.
```

**Hint:**
Use **DFS with parent tracking** or **Union-Find (Disjoint Set Union)**.

**Grade:** Easy

---

### 3. Course Schedule (Topological Sort)

**Problem:**
You are given `n` courses and a list of prerequisite pairs. Return whether it is possible to finish all courses.

**Example:**

```
Input: n = 4, prerequisites = [(1,0),(2,1),(3,2)]
Output: True
Explanation: Order can be 0→1→2→3.
```

```
Input: n = 2, prerequisites = [(0,1),(1,0)]
Output: False
Explanation: Cycle detected.
```

**Hint:**
Think of courses as nodes in a **DAG**. Use **Kahn’s Algorithm (BFS)** or **DFS cycle detection**.

**Grade:** Medium

---

### 4. Minimum Spanning Tree (Kruskal’s Algorithm)

**Problem:**
You are given a connected undirected graph with weighted edges. Find the weight of the **minimum spanning tree**.

**Example:**

```
Input: n = 4, edges = [(0,1,1),(1,2,2),(0,2,2),(2,3,1),(1,3,3)]
Output: 4
Explanation: MST = edges (0,1),(2,3),(1,2) with weight 1+1+2=4.
```

**Hint:**
Sort edges by weight and use **Union-Find** to avoid cycles.

**Grade:** Medium-Hard

---

### 5. Number of Islands (Graph Traversal)

**Problem:**
Given a `m x n` grid of `'0'` (water) and `'1'` (land), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands (4-directionally).

**Example:**

```
Input:
grid = [
 ["1","1","0","0"],
 ["1","0","0","1"],
 ["0","0","1","1"],
 ["0","0","0","0"]
]
Output: 3
```

**Hint:**
Use **DFS or BFS flood-fill** to mark visited cells.

**Grade:** Easy-Medium

---

👉 Do you want me to also provide **Python starter templates** (function skeletons) for each of these problems so you can directly practice coding them?
