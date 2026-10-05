class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token in ops:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(token))

        return int(stack[-1])