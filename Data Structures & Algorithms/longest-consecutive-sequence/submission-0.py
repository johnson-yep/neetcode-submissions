class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sortedNums = sorted(nums)
        prev = sortedNums[0]

        longest = 1
        curr = 1
        for i in range(1, len(nums)):
            if prev+1 == sortedNums[i]:
                curr += 1
            elif prev == sortedNums[i]:
                continue
            else:
                curr = 1
            
            longest = max(longest, curr)
            prev = sortedNums[i]
            
        return longest