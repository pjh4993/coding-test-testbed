"""LFU Cache.

Design a data structure that supports:

- get(key) -> return value if exists, else -1
- put(key, value) -> insert/update key
  When capacity is full, evict the **least frequently used** key. If a tie, evict the least recently used among them.

"""

from collections import OrderedDict, defaultdict


class LFUCache:
    """LFU Cache."""

    def __init__(self, max_size: int):
        """Initialize the LFU Cache."""

        self.max_size = max_size
        self.kv = {}
        self.freq_buckets = defaultdict(OrderedDict)
        self.min_freq = 0

    @property
    def capacity(self) -> int:
        """Get the size of the cache."""
        return len(self.kv)

    def _touch(self, key: int):
        """Touch the key to increase the frequency."""

        # update frequency
        value, freq = self.kv[key]
        freq += 1
        self.kv[key] = (value, freq)

        # move to new bucket
        bucket = self.freq_buckets[freq]
        bucket.pop(key)
        if not bucket:
            del self.freq_buckets[freq]
            if self.min_freq == freq:
                self.min_freq += 1


        self.freq_buckets[freq][key] = None

    def put(self, key: int, value: int):
        """Put the key and value into the cache."""

        if self.max_size == 0:
            return

        if key in self.kv:
            _, freq = self.get(key)
            self.kv[key] = (value, freq)
            self._touch(key)
            return

        if self.capacity == self.max_size:
            k_evicted, _ = self.freq_buckets[self.min_freq].popitem(last=False)
            del self.kv[k_evicted]
            if not self.freq_buckets[self.min_freq]:
                del self.freq_buckets[self.min_freq]

        self.kv[key] = (value, 1)
        self.freq_buckets[1][key] = None
        self.min_freq = 1

    def get(self, key: int) -> int:
        """Get the value of the key from the cache."""

        if key not in self.kv:
            return -1

        self._touch(key)
        return self.kv[key][0]


def solution(size: int, cmds: list[str], args: list[tuple[int, ...]]) -> list[int]:
    """LFU Cache.

    Args:
        cmds: list[str] -> cmd, key, value
        args: list[tuple[int, ...]] -> args
        size: int -> size of the cache

    Returns:
        list[int]: result of the commands

    """

    cache = LFUCache(size)
    results = []

    for cmd, arg in zip(cmds, args, strict=True):
        if cmd == "put":
            cache.put(arg[0], arg[1])
        elif cmd == "get":
            results.append(cache.get(arg[0]))

    return results
