class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-1):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            
            while l < r:
                s = nums[l]+nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        
        return res

            

