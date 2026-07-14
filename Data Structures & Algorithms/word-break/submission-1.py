class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False] * (len(s) + 1)
        arr[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if arr[i]:
                    break
                wLen = len(word)
                if wLen <= i:
                    arr[i] = arr[i - wLen] and word == s[i - wLen: i]
        return arr[-1]
