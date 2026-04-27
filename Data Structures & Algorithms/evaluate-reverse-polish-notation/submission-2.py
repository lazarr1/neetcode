class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['*', '/', '-', '+']

        for char in tokens:

            print(stack)
            if char in operators:
                right = stack.pop()
                left = stack.pop()
            else:
                stack.append(int(char))
                continue

            if char == '*':
                stack.append(left * right)
            elif char == '+':
                stack.append(left + right)
            elif char == '-':
                stack.append(left - right)
            elif char == '/':
                stack.append(int(left / right))


        print(stack)
        return stack.pop()