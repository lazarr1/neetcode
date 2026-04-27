class Solution:
    
    #{1: 3, 2:2, 3:1}
    #sort the dictionary, by value
    #create array from dictionary
    #O(nlogn)

    #O(klogn)
    #create hashmap and heapify the bitch
    #heapop k times
    #klogn runtime!!


    #BUCKET SORT O(N) !!!!
    #shown below

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq_bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)

        #for num, count
        for n,c in count.items():
            freq_bucket[c].append(n)

        ans = []
        for i in range(len(nums), -1,-1):
            for n in freq_bucket[i]:
                ans.append(n)
                if(len(ans) == k):
                    return ans

        # return None
        