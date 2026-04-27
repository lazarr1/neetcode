class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        currBank = 0
        minL = height[l]
        test = set()
        while l < len(height) and r+1 < len(height):
            r += 1
            curr = height[r]
            # print(l, r)
            if minL > curr:
                currBank += minL - curr
            else:
                # print('here', currBank)
                ans += currBank
                currBank = 0
                test.add((l, r))
                l = r
                minL = height[l]

        l, r = len(height) - 1, len(height) - 1
        currBank = 0
        minR = height[r]

        while l > 0 and r > 0:
            l -= 1
            curr = height[l]

            if minR > curr:
                currBank += minR - curr
            else:
                if (l, r) not in test:
                    ans += currBank
                currBank = 0
                r = l
                minR = height[r]
        

        return ans
