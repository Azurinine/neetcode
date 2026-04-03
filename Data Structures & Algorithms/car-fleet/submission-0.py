class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p, s = zip(*sorted(zip(position, speed)))
        timeToDest = [(target - p[i])/s[i] for i in range(len(s))]

        fleets, cTime = 1, timeToDest[-1]
        for i in range(len(s) - 2, -1, -1):
            if timeToDest[i] > cTime:
                cTime = timeToDest[i]
                fleets += 1
        
        return fleets



