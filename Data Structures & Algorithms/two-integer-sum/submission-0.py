class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}

        for i in range(len(nums)):
            x = target-nums[i]
            if nums[i] in req:
                return [req[nums[i]], i]
            req[x] = i
        
        return None
        