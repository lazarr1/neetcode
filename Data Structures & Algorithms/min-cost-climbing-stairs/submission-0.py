class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        costToStair = [0] * len(cost)
        costToStair[0] = cost[0]
        costToStair[1] = cost[1]

        for i in range(2, len(cost)):
            costToStair[i] = min(costToStair[i - 1], costToStair[i-2]) + cost[i]

        return min(costToStair[-1], costToStair[-2])