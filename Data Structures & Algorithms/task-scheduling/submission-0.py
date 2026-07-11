class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque, Counter

        h = [-v for _, v in Counter(tasks).items()]
        heapq.heapify(h)

        q = deque()
        # XXYY, n = 2
        # cycles = 3
        # h = [], q = [(3, -1), (4, -1)]
        print(h)

        cycles = 0
        while q or h:
            if q and q[0][0] == cycles:
                heapq.heappush(h, q.popleft()[1])
            if h:
                freq = heapq.heappop(h) + 1
                if freq:
                    q.append((cycles + n + 1, freq))

            cycles += 1
        
        return cycles
        
