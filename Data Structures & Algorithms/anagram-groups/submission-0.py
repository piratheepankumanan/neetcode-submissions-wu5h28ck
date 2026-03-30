class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array1 = []
        for i in strs:
            ar = sorted(list(i))
            temp_array = []
            for j in strs:
                ar2 = sorted(list(j))
                if ar == ar2:
                    temp_array.append(j)
            if temp_array not in array1:
                array1.append(temp_array)
        return array1