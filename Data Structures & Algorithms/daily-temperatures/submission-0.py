class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []

        for i, x in enumerate(temperatures):
            while len(stack) and stack[-1][1] < x:
                idx, oldT = stack.pop()
                result[idx] = i - idx
            stack.append((i, x))
        return result