class Solution:
    def isValid(self, s: str) -> bool:
        # test solution submission for ReLeet
        brackets = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in brackets:
                if not stack:
                    return False
                popped = stack.pop()
                print(popped)
                print(brackets[char])
                if popped != brackets[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0