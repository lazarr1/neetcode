class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key=lambda x: x[0])
        print(intervals)

        i = 0
        while i < (len(intervals)):
            curr = intervals[i]

            if i + 1 == len(intervals):
                ans.append(curr)
                break
            
            ans.append(curr)
            i+=1

            while i < len(intervals) and ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
                i += 1

        return ans