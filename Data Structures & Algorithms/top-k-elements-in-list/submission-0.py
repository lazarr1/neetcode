class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {} key: num, val: freq
        # {} sort() & look at top k freqs O(nlogn)
        # return

        # {} --> 
        # [] --> freqs
        freqs = {}
        fqnc = [[] for _ in range(len(nums))]
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
            freq = freqs[num] - 1


            fqnc[freq].append(num)


        ret = set()
        i = len(nums) - 1 
        while len(ret) < k and i >= 0:
            ret.update(fqnc[i])
            i -= 1

        return list(ret)
                    
