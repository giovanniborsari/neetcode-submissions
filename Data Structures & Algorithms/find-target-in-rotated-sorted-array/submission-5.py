class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        #Check if target is one of the edges
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        #Basic condition for binary search
        while l <= r:
            #Calculate mid
            m = (l+r)//2
            if nums[m] == target:
                return m
            #Look at left part of the array
            if nums[l] <= nums[m]:
                #Look at the right part of the array
                if target > nums[m] or target < nums[l]:
                    l = m+1
                #Look at the left part of the array
                else:
                    r = m-1
            #Look at right part of the array
            else:
                #Look at the left part of the array
                if target < nums[m] or target > nums[r]:
                    r = m -1 
                #Look at the right part of the array
                else:
                    l = m+1
                
        return -1
        
        