class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 : 1 : 1
        # 2 : 1 1 or 2 : 2
        # 3 : 1 1 1 or 2 1 or 1 2 : 3
        # 4 : 1 1 1 1 or 2 1 1 or 1 1 2 or 1 2 1 or 2 2 : 5
        # 4 : 1 3=[3] or 2 2=[2] = 5 --> no double counting

        # 5 : 1 5=[4] or 2 3=[3] = 8?
        # 1 1 1 1 1 or 2 1 1 1 or 1 2 1 1  or 1 1 2 1 or 1 1 1 2 or 2 1 2 or 2 2 1 or 1 2 2
        # 5 : 1 1 1 1 1 or 2 + [1 1 1]=3 or 1 2 [1 1] = 2 or 2=[1 1] 2 1 or 3[1 1 1] 2 = 1 + 3 + 2 + 2 + 3 =  11
        # 6 : 1 1 1 1 1 1 : 1 11=[] or 2 5=[] : 16?
        cache = [1 for i in range(max(4, n))]
        cache[1] = 2
        cache[2] = 3

        for i in range(3, n):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n - 1]