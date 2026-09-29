class Solution:
    def isValid(self, s: str) -> bool:
        p = {"]":"[", ")":"(", "}":"{"}

        stack = []

        for c in s:
            if c in p:
                if stack and stack[-1] == p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True

        