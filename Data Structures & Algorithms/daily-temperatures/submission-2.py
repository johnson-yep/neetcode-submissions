class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0]*n
        stack = []

        for i in range(n):
            temp = temperatures[i]
            
            while stack and temp > stack[-1][0]:
                print(stack[-1])
                t, index = stack.pop()
                results[index] = i - index
            
            stack.append((temp, i))

        return results
