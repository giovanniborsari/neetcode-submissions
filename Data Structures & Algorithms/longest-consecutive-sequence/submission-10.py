class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Default longest is 0 (empty list)
        longest = 0
        #Hash Set to look for values
        hashSet = set(nums) #O(N)

        #Look for every number inside the hash set
        for n in hashSet: #O(N)

            #If n-1 is not in the hash set, assume
            #n is the first number in the sequence
            if n-1 not in hashSet: 
                current = n

                #Check if next element is available
                while current + 1 in hashSet: 
                    current += 1

                #Difference from current to starting n    
                longest = max(longest, current - (n-1))

        return longest