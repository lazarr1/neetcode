class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            fighter1 = -heapq.heappop(stones)
            fighter2 = -heapq.heappop(stones)

            if fighter1 == fighter2:
                continue
            elif fighter1 > fighter2:
                result = fighter1 - fighter2
            else:
                result = fighter2 - fighter1

            heapq.heappush(stones, -result)

        return -stones[0] if stones else 0



        
            