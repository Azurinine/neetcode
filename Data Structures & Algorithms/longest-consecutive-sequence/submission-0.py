class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_seq = 1
        seq_set = {}

        for num in nums:
            if num in seq_set:
                continue
            
            prev = num - 1
            nex = num + 1
            if prev in seq_set and nex in seq_set:
                seq_set[num] = 1
                prev_seq = seq_set[prev] 
                while(True):
                    if nex + 1 not in seq_set:
                        break
                    nex += 1
                new_seq = prev_seq + 1 + seq_set[nex]
                seq_set[nex] = new_seq

                max_seq = max(max_seq, new_seq)

            elif prev in seq_set:
                curr_seq = seq_set[prev]
                new_seq = curr_seq + 1
                seq_set[num] = new_seq

                if new_seq > max_seq:
                    max_seq = new_seq
            elif nex in seq_set:
                seq_set[num] = 1
                while (True):
                    if nex + 1 not in seq_set:
                        break
                    nex += 1
                new_seq = seq_set[nex] + 1
                seq_set[nex] = new_seq

                max_seq = max(max_seq, new_seq)
            else:
                seq_set[num] = 1
        
        return max_seq
            