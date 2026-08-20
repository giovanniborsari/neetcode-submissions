class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #length of output array
        product = [1] * len(nums)
        
        #prefix multiplication

        #prefix of first index is 1 by default
        left = 1
        for i in range(len(nums)):
            #insert prefix to index i in the array
            product[i] = left
            #update prefix by multiplying previous by the next one
            left *= nums[i]
        
        #postfix multiplication
        right = 1
        #iterate the array backwards 
        for i in range(len(nums) -1, -1, -1):
            #multiply prefix by postfix in index "i"
            product[i] *= right
            #update postfix by multiplying the previous by the next one
            right *= nums[i]
        
        return product
        
        
              
