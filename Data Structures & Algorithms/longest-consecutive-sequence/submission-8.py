class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #If list in empty just return 0
        if not nums:
            return 0

        #Default longest is 1 (the number itself)
        longest = 1
        #Hash Set to look for values
        hashSet = set(nums)

        #Look for every number inside the hash set
        for n in hashSet:

            #If n-1 is not in the hash set, assume
            #n is the first number in the sequence
            if n-1 not in hashSet:
                #starts at 1 (number itself)
                seq = 1
                current = n

                #while next number is available 
                #keep incrementing seq
                while current + 1 in hashSet:
                    current += 1
                    seq += 1
                    longest = max(longest, seq)

        return longest