class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        hashSet = set(nums) #O(N)

        for n in hashSet: #O(N)

            if n-1 not in hashSet: 
                current = n

                while current + 1 in hashSet: 
                    current += 1
  
                longest = max(longest, current - (n-1))

        return longest