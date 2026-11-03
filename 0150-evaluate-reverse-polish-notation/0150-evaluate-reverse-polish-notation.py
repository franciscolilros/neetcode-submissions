class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(float(i))
            elif len(i) > 1 and i[0] == "-":
                stack.append(- float(i[1:]))
            elif i == "+":
                temp = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif i == "-":
                temp = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif i == "*":
                temp = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif i == "/":
                temp = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(temp))
        return int((stack[0]))