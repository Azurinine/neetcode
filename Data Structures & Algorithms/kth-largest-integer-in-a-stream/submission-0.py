class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        return heapq.nlargest(self.k, self.h)[-1]        
