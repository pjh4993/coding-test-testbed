iPerfect 👍 Let’s start with **Sorting & Searching** problems. I’ll give you **classic coding test problems**, each with a short description, constraints, and hints. You can try solving them in **Python**.

---

# 🗂 Sorting & Searching Practice Problems

## 1. **Sort Colors (a.k.a. Dutch National Flag Problem)**

**Problem:**
You are given an array `nums` with values `0`, `1`, and `2`, representing colors (red, white, blue). Sort the array in-place so that `0`s come first, then `1`s, then `2`s.

**Example:**

```python
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Hints:**

* Don’t use built-in `.sort()`.
* Think of **3 pointers**: one for start (0s), one for end (2s), one moving through the array.
* O(n) time, O(1) space.

---

## 2. **Kth Largest Element in an Array**

**Problem:**
Find the k-th largest element in an unsorted array.

**Example:**

```python
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Hints:**

* Approach 1: Sort the array → `nums[-k]` (O(n log n)).
* Approach 2: Use a **heap** (min-heap of size k).
* Approach 3: Quickselect (average O(n), worst O(n²)).

---

## 3. **Meeting Rooms II (Interval Scheduling)**

**Problem:**
Given an array of meeting time intervals `[[s1,e1],[s2,e2],...]`, find the minimum number of conference rooms required.

**Example:**

```python
Input: [[0,30],[5,10],[15,20]]
Output: 2
```

**Hints:**

* Sort start times and end times separately.
* Use two pointers: move end pointer when a meeting finishes.
* This is an application of **sorting + greedy**.

---

## 4. **Search in Rotated Sorted Array**

**Problem:**
Given a rotated sorted array (no duplicates) and a target, return its index, or `-1` if not found.

**Example:**

```python
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Hints:**

* Modified **binary search**.
* One half is always sorted; decide which half to explore.

---

## 5. **Merge Intervals**

**Problem:**
Given an array of intervals, merge all overlapping intervals.

**Example:**

```python
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Hints:**

* Sort by start time.
* Merge if `current.start <= previous.end`.

---

✅ Suggestion: Try solving **Problem 1 (Sort Colors)** first — it’s short but introduces the idea of **in-place sorting with multiple pointers**, which is a recurring trick in coding tests.

Would you like me to also provide **step-by-step Python templates (skeleton code + hints inline)** for these so you can fill in the logic, or do you prefer just the problem statements and hints?
