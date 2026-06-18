class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenNum = {}

        for n in nums:
            if n in seenNum:
                return True
            
            seenNum[n] = True
            
        return False
        