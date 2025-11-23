Awesome — here are **Python solutions with clear explanations** for each Hashing & Data Structures problem you picked.

---

## 1) Two Sum (Easy)

### Idea

Scan once while keeping a **hash map: value → index**. For each `x`, check if `target - x` is already seen; if yes, return the pair of indices.

### Code

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []  # or raise if guaranteed to exist
```

### Why it works

At index `i`, if a complement `need` was seen at index `j`, then `nums[j] + nums[i] = target`. The map ensures O(1) average lookup.

### Complexity

* **Time:** O(n)
* **Space:** O(n)

---

## 2) Longest Substring Without Repeating Characters (Medium)

### Idea

Use **sliding window** with a map `last_index[char]` to remember the most recent index of each character. Expand `r`, and when a duplicate appears, move `l` to `max(l, last_index[char] + 1)` to maintain uniqueness.

### Code

```python
def length_of_longest_substring(s):
    last = {}
    l = best = 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1
        last[ch] = r
        best = max(best, r - l + 1)
    return best
```

### Why it works

The window `[l, r]` always has unique characters. If we see a duplicate `ch`, jumping `l` past its last seen index preserves correctness and linear progress.

### Complexity

* **Time:** O(n)
* **Space:** O(min(n, alphabet))

---

## 3) Subarray Sum Equals K (Medium)

### Idea

Let `pref[i]` be the sum of `nums[:i]`. For each index, count how many previous prefix sums equal `pref[i] - k`. Maintain a frequency map of prefix sums while scanning.

### Code

```python
from collections import defaultdict

def subarray_sum_equals_k(nums, k):
    count = 0
    pref = 0
    freq = defaultdict(int)
    freq[0] = 1  # empty prefix
    for x in nums:
        pref += x
        count += freq[pref - k]
        freq[pref] += 1
    return count
```

### Why it works

If `pref[j] - pref[i] = k`, then `nums[i:j]` sums to `k`. For each `pref[j]`, the number of valid starts `i` is exactly how many times `pref[j] - k` has appeared.

### Complexity

* **Time:** O(n)
* **Space:** O(n)

---

## 4) Group Anagrams (Medium)

### Idea

Anagrams share the same **signature**. Use either:

* Sorted string as key, or
* **Character frequency tuple** (robust & O(L) per word for fixed alphabet).

### Code (frequency signature)

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        # assuming lowercase a-z; adapt length if needed
        count = [0] * 26
        for ch in w:
            count[ord(ch) - 97] += 1
        groups[tuple(count)].append(w)
    return list(groups.values())
```

*(If arbitrary Unicode, prefer `key = ''.join(sorted(w))` for simplicity.)*

### Why it works

All anagrams produce the exact same key (either sorted characters or identical frequency vector), so they land in the same bucket.

### Complexity

* **Time:** O(m · L) with frequency key (m = number of words, L = average length)

  * Sorted-key version: O(m · L log L)
* **Space:** O(m · L) to store results/keys

---

## 5) LFU Cache (Hard)

### Idea

We need **O(1) average** `get`/`put` while evicting the **Least Frequently Used** item (break ties by **Least Recently Used** within that frequency). Use:

* `kv`: key → (value, freq)
* `freq_buckets`: freq → **OrderedDict** of keys (preserves recency within the same freq)
* `min_freq`: smallest freq currently present (for O(1) eviction)

On `get(key)`:

1. If missing, return -1.
2. Otherwise, remove key from current freq bucket, increment its freq, and reinsert to the next bucket’s OrderedDict (becomes most recent in that freq). Update `min_freq` if needed.

On `put(key, value)`:

1. If capacity==0, do nothing.
2. If key exists, update value and call `get(key)` to bump freq.
3. Else, if full, evict the **LRU** key in the `min_freq` bucket (leftmost of its OrderedDict).
4. Insert the new key with freq=1, set `min_freq=1`.

### Code

```python
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv = {}                 # key -> (value, freq)
        self.freq_buckets = defaultdict(OrderedDict)  # freq -> OrderedDict(key -> None)
        self.min_freq = 0

    def _touch(self, key):
        """Increase a key's freq and move it to the new freq bucket (LRU within freq)."""
        val, f = self.kv[key]
        # remove from old bucket
        bucket = self.freq_buckets[f]
        bucket.pop(key)
        if not bucket:
            del self.freq_buckets[f]
            if self.min_freq == f:
                self.min_freq += 1

        # add to new bucket
        f += 1
        self.kv[key] = (val, f)
        self.freq_buckets[f][key] = None  # rightmost = most recent

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self._touch(key)
        return self.kv[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.kv:
            # update value and bump freq
            val, f = self.kv[key]
            self.kv[key] = (value, f)
            self._touch(key)
            return

        # evict if full
        if len(self.kv) == self.cap:
            # evict LRU in the min_freq bucket: popitem(last=False)
            k_evict, _ = self.freq_buckets[self.min_freq].popitem(last=False)
            del self.kv[k_evict]
            if not self.freq_buckets[self.min_freq]:
                del self.freq_buckets[self.min_freq]

        # insert new key with freq = 1
        self.kv[key] = (value, 1)
        self.freq_buckets[1][key] = None
        self.min_freq = 1
```

### Why it works

* **LFU**: Frequencies are explicit in `kv` and `freq_buckets`. We evict from the bucket indicated by `min_freq`.
* **LRU within same freq**: `OrderedDict` maintains insertion recency; the **leftmost** item is the least recent among keys with the same frequency.
* **O(1) operations**: Hash lookups and OrderedDict operations (`popitem`, `pop`, assignment) are O(1) average.

### Complexity

* **Time:** O(1) average for `get` and `put`
* **Space:** O(capacity)

---

If you want, I can bundle these into a small **practice harness** (randomized tests & a CLI) so you can run/verify each solution quickly — or we can move on to **Graphs** or **DP** next with the same structure.
