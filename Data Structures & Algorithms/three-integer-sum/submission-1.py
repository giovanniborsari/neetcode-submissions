class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for i in range(len(nums) - 2):
            #skip duplicate pivot elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            #left index is the one after i
            left = i + 1
            #right index is the last one
            right = len(nums) - 1

            #when left == rigth we checked the full list
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                #we need a smaller number in the sum
                if total > 0:
                    right -= 1
                #we need a larger number in the sum
                elif total < 0:
                    left += 1
                else:
                    #append the combination to the result
                    result.append([nums[i], nums[left], nums[right]])

                    #skip duplicates, since list is sorted
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #update left and right to look for new combinations
                    left += 1
                    right -= 1

        return result



        