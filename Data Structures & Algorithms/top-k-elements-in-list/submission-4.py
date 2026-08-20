class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize an empty hash set
        count = {}
        #Array of buckets where index represents frequency (0 to len(nums))
        #values[i] holds all numbers that appear exactly 'i' times
        values = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            #Increments count of n every time it appears
            count [n] = 1 + count.get(n, 0)
        
        # Append each number to the bucket corresponding to its frequency
        for n,c in count.items():
            values[c].append(n)

        res = []
        
        #Iterates the values backwards, so first appearance is the highest freq
        for i in range(len(values) -1, 0, -1):
            for n in values[i]:
                res.append(n)
                # if res length is the same as k we have all the desired elements
                if len(res) == k:
                    return res

        