class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_set = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in list_set:
                 list_set.remove(s[left])
                 left += 1
            w = (right - left) + 1
            longest = max(longest, w)
            list_set.add(s[right])
        return longest
