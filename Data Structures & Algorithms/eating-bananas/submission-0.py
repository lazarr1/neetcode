class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMax = max(piles)

        def canEatInH(k, h):
            for pile in piles:
                h -= math.ceil(pile / k)

            return h >= 0

        
        l = 1
        r = kMax

        while l <= r:
            mid = (l + r) // 2

            if canEatInH(mid, h):
                r = mid - 1

            else:
                l = mid + 1

        return l