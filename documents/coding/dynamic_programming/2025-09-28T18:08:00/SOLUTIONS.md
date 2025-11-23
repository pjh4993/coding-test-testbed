Awesome — here are clean, interview-ready **solutions with explanations** for the 5 DP problems.
For each: **Idea → Code → Why it works → Complexity.**

---

# 1) Climbing Stairs

## Idea

Number of ways to reach step `i` equals ways to reach `i-1` (take 1 step) plus ways to reach `i-2` (take 2 steps). This is Fibonacci with `dp[0]=1` (stay put), `dp[1]=1`.

## Code

```python
def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    a, b = 1, 1  # dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Why it works

Each path to step `i` must come from `i-1` or `i-2`. Summing those counts gives the total. Using two variables implements the Fibonacci recurrence in O(1) space.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

---

# 2) House Robber

## Idea

At house `i`, choose max of:

* **Skip** `i`: total = best up to `i-1`
* **Rob** `i`: total = best up to `i-2` + `nums[i]`

## Code

```python
from typing import List

def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

## Why it works

The optimal substructure: the best plan up to `i` depends only on `i-1` and `i-2`. Overlapping subproblems (prefixes) are captured by the rolling DP.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

---

# 3) Coin Change (Minimum Coins)

## Idea

Unbounded knapsack style: for each amount `a`, try every coin `c` and relax:
`dp[a] = min(dp[a], dp[a - c] + 1)` if `a >= c`. Initialize `dp[0]=0`, others to `inf`.

## Code

```python
from math import inf
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a >= c and dp[a - c] != inf:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == inf else dp[amount]
```

## Why it works

`dp[a]` represents the optimal answer for sub-amount `a`. Any optimal solution ends with some coin `c`; removing it leaves subproblem `a-c`. Taking the best over all `c` yields optimality.

## Complexity

* **Time:** O(amount × #coins)
* **Space:** O(amount)

---

# 4) Longest Increasing Subsequence (Length)

## Idea (O(n log n) patience sorting)

Maintain `tails[k]` = smallest possible tail value of an increasing subsequence of length `k+1`. For each `x`, binary-search the first `k` with `tails[k] >= x` and set `tails[k]=x`. The length of `tails` is the LIS length.

## Code

```python
from bisect import bisect_left
from typing import List

def length_of_LIS(nums: List[int]) -> int:
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

## Why it works

Replacing a tail with a smaller value keeps future extension opportunities maximal while preserving subsequence lengths. Binary-search maintains the minimal possible tail for each length, so the final number of piles equals LIS length.

## Complexity

* **Time:** O(n log n)
* **Space:** O(n)

*(If you need a pure DP version during interviews, the classic O(n²) approach with `dp[i]=1+max(dp[j]) for j<i and nums[j]<nums[i]` also works.)*

---

# 5) Edit Distance (Levenshtein Distance)

## Idea

Let `dp[i][j]` be the min operations to convert `word1[:i]` → `word2[:j]`.
Transition from:

* **Insert**: `dp[i][j-1] + 1`
* **Delete**: `dp[i-1][j] + 1`
* **Replace/Match**: `dp[i-1][j-1] + (word1[i-1] != word2[j-1])`

Base: `dp[i][0]=i`, `dp[0][j]=j`.

## Code

```python
def edit_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(
                dp[i][j - 1] + 1,      # insert
                dp[i - 1][j] + 1,      # delete
                dp[i - 1][j - 1] + cost  # replace / match
            )
    return dp[m][n]
```

*(Space-optimization tip: keep only previous and current rows to reduce to O(n) space.)*

## Why it works

Any optimal sequence of edits ends in exactly one of {insert, delete, replace/match}. The recurrence captures these last operations, and the DP table ensures all prefixes are solved once.

## Complexity

* **Time:** O(m·n)
* **Space:** O(m·n) (or O(n) with row compression)

---

## Quick Recap Patterns

* **Count paths/ways →** Fibonacci-like linear DP (Climbing Stairs).
* **Pick/non-pick on a line →** 1D DP with `prev1/prev2` (House Robber).
* **Unbounded choices to hit a target →** 1D knapsack (Coin Change).
* **Best subsequence structure →** patience sorting + binary search (LIS).
* **Edit/alignment of strings →** 2D DP over prefixes (Edit Distance).

If you want, I can bundle these into a small **`dp_solutions.py`** module with unit tests matching your generated Parquet cases.
