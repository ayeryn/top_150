# 295

from heapq import *


class MedianFinder:
    def __init__(self):
        self.min_heap = []  # largest at front: insert -num
        self.max_heap = []  # smallest at front

    def addNum(self, num: int) -> None:
        # keep the extra element in max
        # keep len diff <= 1
        if len(self.max_heap) == 0:  # First insertion
            heappush(self.max_heap, num)

        elif num < self.max_heap[0]:  # Smaller half
            heappush(self.min_heap, -num)

            # Balance length if needed
            if len(self.min_heap) > len(self.max_heap):
                move = -heappop(self.min_heap)
                heappush(self.max_heap, move)

        else:  # Larger half
            heappush(self.max_heap, num)

            # Update length if needed
            if len(self.max_heap) - len(self.min_heap) > 1:
                move = heappop(self.max_heap)
                heappush(self.min_heap, -move)

    def findMedian(self) -> float:
        """
        Odd : max_heap[0]
        Even: average of max(min_heap) and min(max_heap)
        """
        return (
            self.max_heap[0]
            if len(self.max_heap) > len(self.min_heap)
            else (self.max_heap[0] + -self.min_heap[0]) / 2
        )

    pass
