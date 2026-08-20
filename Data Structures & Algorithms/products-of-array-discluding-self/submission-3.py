class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #length of output array
        product = [1] * len(nums)
        
        #prefix multiplication
        left = 1
        for i in range(len(nums)):
            product[i] = left
            left *= nums[i]
        
        #postfix multiplication
        right = 1
        for i in range(len(nums) -1, -1, -1):
            product[i] *= right
            right *= nums[i]
        
        return product
        
        
              
