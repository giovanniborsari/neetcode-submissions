class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        longest = 1
        hashSet = set(nums)

        for n in hashSet:

            if n-1 not in hashSet:
                seq = 1
                current = n

                while current + 1 in hashSet:
                    current += 1
                    seq += 1
                    longest = max(longest, seq)

        return longest