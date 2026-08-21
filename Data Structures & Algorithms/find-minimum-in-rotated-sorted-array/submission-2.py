class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Assume the first result is the min
        res = nums[0]
        #Set left and right index
        l, r = 0, len(nums) - 1

        while l <= r:
            #Since sorted before, num[l] is the min
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #Finds min index
            m = (l + r) // 2
            res = min(res, nums[m])
            #min is in between m and r
            if nums[m] >= nums[l]:
                l = m + 1
            #min is in between l and m 
            else:
                r = m - 1
        return res