
import heapq
from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            # If the earliest ending meeting is done before this one starts, reuse the room
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

def main():
    raw_intervals =   [[1,2],[2,3],[3,4],[4,5]]
    intervals = [Interval(start, end) for start, end in raw_intervals]

    sol = Solution()
    result = sol.minMeetingRooms(intervals)
    print("Minimum number of days (rooms) required:", result)

if __name__ == "__main__":
    main()