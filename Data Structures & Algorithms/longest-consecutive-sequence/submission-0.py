class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_num = 0
        for i in numset:
            Sequence_1 = 0
            if i - 1 not in numset:
                Sequence_1 = 1
                current_num = i
                while current_num + 1 in numset:
                    current_num += 1
                    Sequence_1 += 1
            longest_num = max(longest_num, Sequence_1)
        
        return longest_num

