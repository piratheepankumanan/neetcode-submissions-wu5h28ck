class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_array = sorted(list(s))
        string_array2 = sorted(list(t))
        if string_array == string_array2:
            return True
        else:
            return False