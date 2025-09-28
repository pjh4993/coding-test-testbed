Great choice 👍 Dynamic Programming (DP) is one of the most important areas for coding tests.
Here are **5 hand-picked DP problems** with problem statements, examples, hints, and difficulty grades:

---

### 1. **Climbing Stairs (Basic DP)**

**Problem:**
You are climbing a staircase. It takes *n* steps to reach the top. Each time you can climb either **1** or **2** steps. In how many distinct ways can you climb to the top?

**Example:**
```
Input: `n = 3`
Output: `3`
Explanation: (1+1+1), (1+2), (2+1)
```

**Hint:**
This is essentially the Fibonacci sequence. Define `dp[i] = number of ways to reach step i`.

**Grade:** Easy ⭐

---

### 2. **House Robber**

**Problem:**
You are a robber planning to rob houses along a street. Each house has some amount of money, but you cannot rob two adjacent houses. Find the maximum amount you can rob.

**Example:**
```
Input: `nums = [2,7,9,3,1]`
Output: `12` (Rob houses 2 + 9 + 1)
```

**Hint:**
DP relation: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

**Grade:** Easy-Medium ⭐⭐

---

### 3. **Coin Change**

**Problem:**
You are given coins of different denominations and a target amount. Find the **minimum number of coins** needed to make the target. If it’s not possible, return `-1`.

**Example:**
```
Input: `coins = [1, 2, 5], amount = 11`
Output: `3` (11 = 5 + 5 + 1)
```

**Hint:**
Unbounded knapsack style.
Transition: `dp[x] = min(dp[x], dp[x - coin] + 1)`

**Grade:** Medium ⭐⭐⭐

---

### 4. **Longest Increasing Subsequence (LIS)**

**Problem:**
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Example:**
```
Input: `nums = [10,9,2,5,3,7,101,18]`
Output: `4` (subsequence: [2,3,7,101])
```

**Hint:**
O(n²) DP: `dp[i] = 1 + max(dp[j]) for j < i and nums[j] < nums[i]`.
(Also solvable in O(n log n) using binary search).

**Grade:** Medium-Hard ⭐⭐⭐⭐

---

### 5. **Edit Distance (Levenshtein Distance)**

**Problem:**
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` into `word2`.
Operations allowed: insert, delete, replace.

**Example:**
```
Input: `word1 = "horse"`, `word2 = "ros"`
Output: `3`
Explanation: horse → rorse (replace) → rose (delete) → ros (delete)
```

**Hint:**
Classic 2D DP:
`dp[i][j] = min(dp[i-1][j] + 1,  dp[i][j-1] + 1,  dp[i-1][j-1] + cost)`

**Grade:** Hard ⭐⭐⭐⭐⭐

---

⚡ These five cover **basic, intermediate, and advanced** DP. If you practice them deeply, you’ll unlock patterns that apply to most DP problems in coding interviews.

👉 Do you want me to also **create Python skeleton code templates** for each of these so you can directly practice filling them in?
