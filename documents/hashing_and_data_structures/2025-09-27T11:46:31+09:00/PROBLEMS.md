Got it ✅ — here are **5 well-known problems** from the **Hashing & Data Structures** category, with the format you asked for:

---

## 1. Two Sum

**Problem:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

**Example:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Hint:**
Use a hash map to store numbers you’ve seen and their indices. For each `x`, check if `target - x` is already in the map.

**Grade:** Easy

---

## 2. Longest Substring Without Repeating Characters

**Problem:**
Find the length of the longest substring without repeating characters.

**Example:**

```
Input: s = "abcabcbb"
Output: 3   # "abc"
```

**Hint:**
Use a sliding window and a hash set (or dictionary) to track characters. Move left pointer whenever you see a duplicate.

**Grade:** Medium

---

## 3. Subarray Sum Equals K

**Problem:**
Given an integer array `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

**Example:**

```
Input: nums = [1,2,3], k = 3
Output: 2   # [1,2] and [3]
```

**Hint:**
Use prefix sum and a hash map. At each step, check how many times `(current_sum - k)` appeared before.

**Grade:** Medium

---

## 4. Group Anagrams

**Problem:**
Given an array of strings, group the anagrams together.

**Example:**

```
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

**Hint:**
Use a hash map where the key is either the **sorted string** or a tuple of **character counts**.

**Grade:** Medium

---

## 5. LFU Cache (Least Frequently Used Cache)

**Problem:**
Design a data structure that supports:

* `get(key)` → return value if exists, else -1
* `put(key, value)` → insert/update key
  When capacity is full, evict the **least frequently used** key. If a tie, evict the least recently used among them.

**Example:**

```
Input:
LFUCache cache = LFUCache(2);
cache.put(1,1);
cache.put(2,2);
cache.get(1);    # returns 1
cache.put(3,3);  # evicts key 2
cache.get(2);    # returns -1
cache.get(3);    # returns 3
```

**Hint:**
Need two hash maps:

* One for key → (value, frequency)
* One for frequency → ordered dictionary (to maintain recency).

**Grade:** Hard

---

👉 Next step: when you’re ready, ask me for the **solutions with full explanations** and I’ll walk you through Python code for each one.

Do you want me to order these by **frequency of appearance in interviews** (so you know which to focus on first)?
