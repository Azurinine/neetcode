class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            x, y = point
            dist = -(x**2 + y**2) ** 0.5
            if len(max_heap) < k:
                heapq.heappush(max_heap, [dist, point])
            elif max_heap[0][0] < dist:
                heapq.heappush(max_heap, [dist,point])
                heapq.heappop(max_heap)
        
        return [pt for _, pt in max_heap]