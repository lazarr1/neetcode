class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openning = ['(', '{', '[']

        closingMatch = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in openning:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                if stack[-1] != closingMatch[char]:
                    return False
                else:
                    stack.pop()

        return not stack