Awesome—here are clean, interview-ready **solutions + explanations** for the 5 greedy problems. Each one includes **Idea → Code → Why it works → Complexity**.

---

## 1) Activity Selection (Maximum Non-Overlapping Intervals)

### Idea

Pick the activity that **finishes earliest**, then keep picking the next activity that **starts after the last chosen one ends**. Sorting by end time leaves maximum room for future choices.

### Code

```python
from typing import List, Tuple

def max_activities(activities: List[Tuple[int, int]]) -> int:
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for s, e in activities:
        if s >= last_end:
            count += 1
            last_end = e
    return count
```

### Why it works

**Exchange argument**: In any optimal solution, the first chosen activity can be replaced by the one that ends earliest without reducing the number of activities; repeating this yields the greedy sequence, which is optimal.

### Complexity

* Sorting: **O(n log n)**
* Scan: **O(n)**
* Total: **O(n log n)**, space **O(1)** (in-place sort aside)

---

## 2) Minimum Number of Coins (Canonical Denominations)

### Idea

For **canonical systems** (like `[1,2,5,10,20,50,100,500,1000]`), always take as many of the **largest denomination** as possible, then move to the next.

### Code

```python
from typing import List

def min_coins(denominations: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    denominations.sort(reverse=True)
    count = 0
    for d in denominations:
        if d <= amount:
            k = amount // d
            count += k
            amount -= k * d
        if amount == 0:
            break
    return count
```

### Why it works

For canonical coin systems, the greedy choice (largest coin first) can be shown to be optimal (proof depends on the coin set’s structure). **Note**: For non-canonical sets, greedy can fail (e.g., `[1,3,4]` for amount `6`).

### Complexity

* Sorting (once): **O(m log m)**, where `m` = #denominations
* Scan: **O(m)**
* Total: **O(m log m)**, space **O(1)**

---

## 3) Fractional Knapsack

### Idea

Sort items by **value/weight ratio** (marginal value) and take as much as you can from the top until the capacity runs out. You may take **fractions**.

### Code

```python
from typing import List

def fractional_knapsack(capacity: int, values: List[float], weights: List[float]) -> float:
    items = [(v / w, v, w) for v, w in zip(values, weights) if w > 0]
    items.sort(reverse=True)  # highest ratio first
    total = 0.0
    remaining = capacity
    for ratio, v, w in items:
        if remaining == 0:
            break
        take = min(w, remaining)
        total += ratio * take   # (v/w) * taken_weight
        remaining -= take
    return total
```

### Why it works

This is a classic case where the **greedy-choice property** holds: taking the highest marginal value first is optimal, and the problem has **optimal substructure** (leftover capacity is the same problem, smaller size). This can be proved by a standard exchange argument.

### Complexity

* Build + sort ratios: **O(n log n)**
* Scan: **O(n)**
* Total: **O(n log n)**, space **O(n)**

---

## 4) Job Sequencing with Deadlines (Unit-time Jobs, Max Profit)

### Idea

Sort jobs by **profit descending**, and for each job, schedule it in the **latest free time slot ≤ its deadline**. Use a disjoint-set (Union-Find) or a simple slot array.

### Code (slot array approach)

```python
from typing import List, Tuple

def max_profit_job_sequencing(jobs: List[Tuple[int, int, int]]) -> int:
    """
    jobs: list of (job_id, deadline, profit)
    returns max total profit
    """
    if not jobs:
        return 0
    # Sort by profit desc
    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    # Find the maximum deadline
    max_deadline = max(d for _, d, _ in jobs_sorted)
    # slots[t] = whether time slot t is occupied (1..max_deadline)
    slots = [False] * (max_deadline + 1)
    total_profit = 0
    for _, deadline, profit in jobs_sorted:
        # Try to place as late as possible
        t = min(deadline, max_deadline)
        while t > 0 and slots[t]:
            t -= 1
        if t > 0 and not slots[t]:
            slots[t] = True
            total_profit += profit
    return total_profit
```

### Why it works

Greedy by profit ensures we never miss a high-value job if it can fit. Scheduling each picked job in the **latest** possible slot preserves earlier slots for other jobs with earlier deadlines. Exchange arguments show any optimal schedule can be transformed into this greedy schedule without reducing profit.

### Complexity

* Sort: **O(n log n)**
* Placement: worst-case **O(n · Dscan)**; with the simple while loop, worst-case `O(n * max_deadline)`.
  With Union-Find (DSU) to find the next free slot, it improves to near **O(n α(n))** after sorting.
* Space: **O(max_deadline)**

---

## 5) Huffman Coding (Optimal Merge Cost)

### Idea

Repeatedly **merge the two least-frequent** symbols; push their combined frequency back. The sum of all merge costs equals the **optimal total weighted path length** (or optimal encoding cost).

### Code

```python
import heapq
from typing import Dict

def huffman_optimal_cost(freq: Dict[str, int]) -> int:
    heap = [f for f in freq.values() if f > 0]
    if not heap:
        return 0
    if len(heap) == 1:
        # Single symbol -> no bits needed; some definitions return 0 cost.
        return 0
    heapq.heapify(heap)
    total_cost = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        total_cost += s
        heapq.heappush(heap, s)
    return total_cost
```

### Why it works

This is a classic **optimal merge pattern**. The **Greedy choice** (always merge two smallest) is optimal; proof uses the **structural optimality** of prefix codes and an exchange argument: in an optimal tree, the two least frequent symbols are siblings at the deepest level. Repeating this yields Huffman’s algorithm.

### Complexity

* Build heap: **O(k)**
* Each of `k−1` merges: heap ops **O(log k)**
* Total: **O(k log k)**, space **O(k)**, where `k` is the number of symbols

---

### Quick sanity checks (optional)

* Activity selection works on sorted-by-end tests and degenerate overlaps.
* Coins: correct for canonical sets (the ones in your tests).
* Fractional knapsack: watch floating precision; compare with a tolerance if needed.
* Job sequencing: if `max_deadline` is huge, consider DSU to reduce placement cost.
* Huffman: returns **total merge cost** (unique), not the specific codes (which may vary).

If you want, I can wrap these into a small **`solutions.py`** module with function names aligned to your test harness and add a **pytest** sample showing how to read your `.parquet` cases and assert the results.
