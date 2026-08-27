class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                leng = 1
                while n+leng in numSet:
                    leng += 1
                longest = max(leng, longest)

        return longest