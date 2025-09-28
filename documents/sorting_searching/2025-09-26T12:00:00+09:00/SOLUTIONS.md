Awesome—here are the same five Sorting/Searching problems with **Python solutions + clear explanations**, including intuition, invariants, and complexity.

---

# 1) Sort Colors (Dutch National Flag)

### Idea

We keep three regions:

* `[0..low-1]` are all `0`s,
* `[low..mid-1]` are all `1`s (processed),
* `[mid..high]` are unknown,
* `[high+1..end]` are all `2`s.

We scan with `mid`.

* If we see `0`, swap it to the `low` side and advance both `low` and `mid`.
* If we see `1`, it’s already in the middle region → just `mid += 1`.
* If we see `2`, swap with `high` and move `high -= 1` (don’t advance `mid` yet, because the swapped-in element is unclassified).

### Code

```python
def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
```

### Why it works

The three-region invariant always holds. We only pass through each element a constant number of times.

**Complexity:** O(n) time, O(1) space.

---

# 2) Kth Largest Element (Quickselect)

### Idea

To find the k-th largest, we look for the element that would be at index `n-k` if the array were sorted ascending.
**Partition step:** pick a pivot and place all `<= pivot` on the left and `> pivot` on the right (Lomuto scheme).

* If pivot index `p` equals `n-k`, we’re done.
* If `p < n-k`, recurse (or iterate) on the right half; else on the left.

### Code

```python
def findKthLargest(nums, k):
    target = len(nums) - k
    l, r = 0, len(nums) - 1

    while True:
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p == target:
            return nums[p]
        elif p < target:
            l = p + 1
        else:
            r = p - 1
```

### Why it works

Partitioning ensures the pivot is in its final sorted position. We only recurse/iterate into the side that could contain the target index.

**Complexity:** Average O(n), worst O(n²) (rare in practice). Space O(1).

> ⚡ Quick alternative: `heapq.nlargest(k, nums)[-1]` (O(n log k)).

---

# 3) Meeting Rooms II (Minimum Rooms)

### Idea

Split starts and ends, sort both. Sweep in time order:

* When a meeting starts before the earliest current meeting ends, we need a new room.
* Otherwise, we can reuse a room (advance the end pointer).

This is a classic “two sorted arrays + two pointers” pattern.

### Code

```python
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)

    rooms = max_rooms = 0
    i = j = 0
    while i < len(starts):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1
    return max_rooms
```

### Why it works

Every time a start precedes the earliest end, intervals overlap → need another room. When an end comes first, a room frees up.

**Complexity:** O(n log n) time (sorting), O(n) space.

---

# 4) Search in Rotated Sorted Array

### Idea

Modified binary search. For any mid:

* One side (left or right) is sorted.
* Check if the target lies within that sorted side’s range; if yes, binary search into it; otherwise search the other side.

### Code

```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m

        # Left side sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # Right side sorted
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
```

### Why it works

Even though the whole array isn’t sorted, at least one half around `mid` is. We exploit that to discard half each step.

**Complexity:** O(log n) time, O(1) space.

---

# 5) Merge Intervals

### Idea

Sort by start. Keep a `merged` list and compare the next interval `(s, e)` to the last merged:

* Overlap if `s <= merged[-1][1]`: update end with `max`.
* Otherwise, push as a new interval.

### Code

```python
def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged
```

### Why it works

Sorting by start guarantees that any overlap for a given interval can only happen with the most recently merged one.

**Complexity:** O(n log n) time, O(n) space (for output).

---

## Quick sanity tests (you can run these)

```python
assert sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
assert findKthLargest([3,2,1,5,6,4], 2) == 5
assert minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
assert search_rotated([4,5,6,7,0,1,2], 0) == 4
assert mergeIntervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
```

---

If you want, I can turn these into a single script with a small CLI to pick which problem to run, or we can move on to the next category (e.g., **Binary Search patterns**, **Heaps/Priority Queues**, or **Dynamic Programming**) with problem sets + solutions.
