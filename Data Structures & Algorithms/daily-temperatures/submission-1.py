class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        minStack = collections.deque()
        minStack.append((temperatures[-1], len(ans)- 1))


        for r in range(len(temperatures) - 2, -1, -1):
            cTemp = temperatures[r]
            maxTemp = minStack[0][0]

            if cTemp >= maxTemp:
                minStack = collections.deque()
                minStack.append((cTemp, r))
                ans[r] = 0
            else:
                while minStack and cTemp >= minStack[-1][0]:
                    minStack.pop()
                
                if minStack:
                    ans[r] = minStack[-1][1] - r
                else:
                    ans[r] = 0 # shouldnt be possible ig
                
                minStack.append((cTemp, r))

        return ans


                





