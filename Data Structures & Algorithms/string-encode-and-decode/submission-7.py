class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            if (length < 10):
                length = "00" + str(length)
            elif (length < 100):
                length = "0" + str(length)

            res += str(length) + word
        return res

    def decode(self, s: str) -> List[str]:
        curr_idx = 0
        res = []
        
        while (curr_idx < len(s)):
            length = int(s[curr_idx : curr_idx + 3])
            start_idx = curr_idx + 3
            end_idx = start_idx + length

            res.append(s[start_idx : end_idx])

            curr_idx = end_idx
        
        return res