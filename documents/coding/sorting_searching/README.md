Great — let’s build an **ideation flow for solving sorting and searching problems** in coding tests. Like with graphs, having a structured thought process avoids guesswork and helps you pick the right algorithm quickly.

---

# 🔹 Step 1: Understand the Problem

Ask:

* Are we looking for **a position** (index) or **a value**?
* Is the input **sorted** or **unsorted**?
* Do we need **exact match** or **approximate (lower bound, closest, etc.)**?
* Are there constraints like **duplicates**, **large input size**, or **streaming data**?

---

# 🔹 Step 2: Recognize Problem Type

Sorting and searching problems usually fall into categories:

### **Sorting**

* **Basic sorting**: just output sorted data (use built-ins unless explicitly asked to implement).
* **Custom sorting**: sort by multiple keys (e.g., frequency, custom comparator).
* **In-place sorting**: memory-limited (QuickSort, HeapSort).
* **Stable sorting**: preserve order of equals (MergeSort, TimSort).

### **Searching**

* **Exact element search**: Find x in sorted array (Binary Search).
* **Range queries**: Find first/last occurrence, count elements ≤ k.
* **Optimization/search on answer**: Binary search on monotonic condition.
* **Search in 2D**: Binary search on matrix / rotated sorted array.
* **Approximate/nearest**: Lower/upper bounds, closest value.

---

# 🔹 Step 3: Match With Known Patterns

* **If input is sorted:** binary search or variations.
* **If unsorted but small:** brute-force linear scan may be acceptable.
* **If unsorted but large:** sort first (O(n log n)) then binary search or use hashing (O(n)).
* **If optimization style ("minimum X that satisfies condition")**: binary search on answer.

---

# 🔹 Step 4: Constraints Check

* **n up to 10^5 or 10^6** → O(n log n) or O(n) needed, avoid O(n²).
* **Memory constraints** → use in-place algorithms.
* **Real-time/streaming** → heaps, quickselect, or online algorithms.

---

# 🔹 Step 5: Build Reusable Templates

1. **Sorting**

   ```python
   arr.sort()  # built-in TimSort, O(n log n)
   ```

   Or with custom key:

   ```python
   arr.sort(key=lambda x: (x[1], -x[0]))
   ```

2. **Binary Search (exact)**

   ```python
   def binary_search(arr, target):
       lo, hi = 0, len(arr)-1
       while lo <= hi:
           mid = (lo+hi)//2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               lo = mid+1
           else:
               hi = mid-1
       return -1
   ```

3. **Binary Search on Answer**

   ```python
   def binary_search_answer(low, high, condition):
       while low < high:
           mid = (low+high)//2
           if condition(mid):
               high = mid   # move left
           else:
               low = mid+1
       return low
   ```

4. **Heap for Selection (e.g., k-th largest)**

   ```python
   import heapq
   def kth_largest(nums, k):
       return heapq.nlargest(k, nums)[-1]
   ```

---

# 🔹 Step 6: Edge Cases & Pitfalls

* Duplicates (first vs last occurrence).
* Empty input.
* Off-by-one errors in binary search.
* Overflow (in other languages, not Python, but good to remember).
* Stability requirements for sorting.

---

# 🔹 Step 7: Debug With Examples

* For binary search: test with `target` smaller than all elements, larger than all, exactly in middle, and duplicates.
* For sorting: test with all equal elements, already sorted, reverse sorted.

---

✅ **Summary Flow**

1. Parse problem → Is it sorting or searching?
2. Check sortedness / monotonicity → pick algorithm.
3. Match to template (binary search, heap, custom sort).
4. Consider constraints (time, space).
5. Handle edge cases.
6. Implement + verify with toy examples.

---

Would you like me to now **pick 5 classic sorting/searching interview problems** (like I did for graph algorithms) and present them with **Problem → Example → Hint → Grade**?
