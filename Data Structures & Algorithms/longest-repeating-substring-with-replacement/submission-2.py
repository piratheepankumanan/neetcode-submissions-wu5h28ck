class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        counts = [0] * 26

        for right in range(len(s)):
            counts[ord(s[right]) - 65] += 1
            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1


            w = (right - left) + 1
            longest = max(longest, w)
        return longest
