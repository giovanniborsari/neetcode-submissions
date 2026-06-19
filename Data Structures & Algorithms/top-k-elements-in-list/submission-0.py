class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNums = {}

        for n in nums:
            if n in hashNums:
                hashNums[n] += 1
            else:
                hashNums[n] = 1

        final = []
        for i in range(k):
            max_key = max(hashNums, key=hashNums.get)
            final.append(max_key)
            hashNums.pop(max_key)  

        return final   

        