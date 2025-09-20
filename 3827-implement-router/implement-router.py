from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()  # FIFO storage of packets
        self.packetSet = set()  # To detect duplicates
        self.destMap = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packetSet:
            return False  # duplicate
        
        # If full, evict oldest
        if len(self.queue) >= self.limit:
            old_src, old_dest, old_ts = self.queue.popleft()
            self.packetSet.remove((old_src, old_dest, old_ts))
            # remove timestamp from destMap using binary search
            idx = bisect.bisect_left(self.destMap[old_dest], old_ts)
            self.destMap[old_dest].pop(idx)
            if not self.destMap[old_dest]:
                del self.destMap[old_dest]

        # Add new packet
        self.queue.append((source, destination, timestamp))
        self.packetSet.add(key)
        bisect.insort(self.destMap[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        src, dest, ts = self.queue.popleft()
        self.packetSet.remove((src, dest, ts))
        idx = bisect.bisect_left(self.destMap[dest], ts)
        self.destMap[dest].pop(idx)
        if not self.destMap[dest]:
            del self.destMap[dest]
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0
        arr = self.destMap[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left
