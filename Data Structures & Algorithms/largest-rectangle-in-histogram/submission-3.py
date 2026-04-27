class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 
        # | |        |
        # |4, a|     |
        # |3, a| --> |
        # |2, a|     | 2, a |
        #  _
        # 

        stack = []
        ans = -1
        for index, height in enumerate(heights):
            area = height
            ans = max(ans, area)

            if not stack:
                stack.append([height, index, area])
                continue

            for index2, rect in enumerate(stack):
                if height >= rect[0]:
                    stack[index2][2] += rect[0]
                elif height < rect[0]:
                    stack[index2][0] = height
                    stack[index2][2] = (index - rect[1] + 1) * height
                    ans = max(ans, stack[index2][2])

                    break

                ans = max(ans, stack[index2][2])

            # print(stack)
            if index2 != len(stack) - 1:
                stack = stack[0:index2+1]
            if stack[-1][0] != height:
                stack.append([height, index, area])

            # print(stack)



        return ans


            


