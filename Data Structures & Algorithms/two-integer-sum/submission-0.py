class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_numbers = {}

        for i, num in enumerate(nums): 
            comp = target - num

            if comp in seen_numbers:

                return [seen_numbers[comp], i]

            seen_numbers[num] = i

        return [] 