class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binarySearch(nums: List[int], find:int):
            l = 0
            r = len(nums) - 1

            while l <= r:
                ptr = l + (r - l) // 2
                if nums[ptr] == find:
                    return ptr
                
                elif nums[ptr] > find:
                    r = ptr - 1
                else:
                    l = ptr + 1
            
            return -1

        for i, num in enumerate(numbers):
            find = target - num

            match = binarySearch(numbers, find)
            if match != -1 and match != i:
                return [i+1, match+1]
        
        return [0, 0]
            
        