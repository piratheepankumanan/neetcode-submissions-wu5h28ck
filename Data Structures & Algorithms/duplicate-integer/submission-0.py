class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        array_fake = []
        for i in nums:
            if i not in array_fake:
                array_fake.append(i)
        if array_fake == nums:
            return False
        if array_fake != nums:
            return True
        

