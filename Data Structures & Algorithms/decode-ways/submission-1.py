class Solution:
    def numDecodings(self, s: str) -> int:      
        # Given s of lenght N how many ways?

        # Ways to do length n - 2 + 1 (if possible)
        # Ways to length n - 1 + 1

        one = 1 if s[0] != "0" else 0
        two = 1

        for i in range(1, len(s)):
            temp = one if s[i] != "0" else 0
            if s[i - 1] == "1" or (s[i - 1] == "2" and int(s[i]) <= 6):
                temp += two
            two, one = one, temp
        
        return one








