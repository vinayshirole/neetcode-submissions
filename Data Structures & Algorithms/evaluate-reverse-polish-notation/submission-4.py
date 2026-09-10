class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ('+', '-', '*', '/'):
                stack.append(tokens[i])
            else:
                number2 = int(stack.pop())
                number1 = int(stack.pop())

                if tokens[i] == '+':
                    stack.append(number1 + number2)
                elif tokens[i] == '-':
                    stack.append(number1 - number2)
                elif tokens[i] == '*':
                    stack.append(number1 * number2)
                else:
                    stack.append(int(number1 / number2))
        output = int(stack.pop())
        return output