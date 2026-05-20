class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(x - y))
        
        return -max_heap[0]