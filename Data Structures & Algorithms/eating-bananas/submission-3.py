class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (right + left) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/k)
            if total_hours <= h:
                right = k
            else: 
                left = k + 1
        return left