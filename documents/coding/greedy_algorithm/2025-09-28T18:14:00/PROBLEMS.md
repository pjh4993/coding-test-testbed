Got it 👍 Here’s the refined version with **examples wrapped in code blocks** for readability:

---

### **1. Activity Selection Problem**

**Problem:**
You are given `n` activities with start and end times. Select the maximum number of non-overlapping activities that can be performed by a single person.

**Example:**

```
Input: [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
Output: 4   # Activities: (1,3), (4,6), (6,7), (8,9)
```

**Hint:**
Sort activities by their ending time, then keep picking the next activity that starts after the previous one ends.

**Grade:** ★★☆☆☆ (Easy–Medium)

---

### **2. Minimum Number of Coins**

**Problem:**
You have denominations `[1, 2, 5, 10, 20, 50, 100, 500, 1000]`. For a given amount, find the minimum number of coins/notes required.

**Example:**

```
Input: amount = 93
Output: 5   # 50 + 20 + 20 + 2 + 1
```

**Hint:**
Always pick the largest possible denomination first (greedy choice).

**Grade:** ★☆☆☆☆ (Easy)

---

### **3. Fractional Knapsack**

**Problem:**
Given weights and values of `n` items, and a maximum capacity `W`, choose items to maximize total value. You can break items (fractions allowed).

**Example:**

```
Input: W = 50, values = [60,100,120], weights = [10,20,30]
Output: 240.0
```

**Hint:**
Sort items by value-to-weight ratio, then take as much as possible in that order.

**Grade:** ★★★☆☆ (Medium)

---

### **4. Job Sequencing with Deadlines**

**Problem:**
Each job has a deadline and profit. You can only do one job at a time, and each job takes 1 unit time. Maximize total profit.

**Example:**

```
Input: Jobs = [(id=1, deadline=4, profit=20),
               (id=2, deadline=1, profit=10),
               (id=3, deadline=1, profit=40),
               (id=4, deadline=1, profit=30)]

Output: Jobs done = [3,1], Max Profit = 60
```

**Hint:**
Sort jobs by profit descending, schedule each job in the latest possible slot before its deadline.

**Grade:** ★★★★☆ (Medium–Hard)

---

### **5. Huffman Coding**

**Problem:**
Given characters with frequencies, build a binary tree to encode characters such that the total encoding cost is minimized.

**Example:**

```
Input: {a:5, b:9, c:12, d:13, e:16, f:45}
Output: Huffman tree with average code length minimized (codes may vary)
```

**Hint:**
Use a min-heap: repeatedly combine the two lowest-frequency nodes until one tree remains.

**Grade:** ★★★★★ (Hard)

---

👉 Would you like me to also prepare **Python implementations** for each of these so you can test them on your own?
