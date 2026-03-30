class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_1 = dict() 
        for i in nums:
            if i not in dict_1:
                new_dict = {i:1}
                dict_1.update(new_dict)
            else:
                dict_1[i] += 1
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        for number, counter in dict_1.items():
            freq[counter].append(number)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
             for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

