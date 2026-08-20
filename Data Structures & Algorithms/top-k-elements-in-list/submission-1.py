class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Empty hash
        hashNums = {}

        for n in nums:
            #Increment count if n is already present
            if n in hashNums:
                hashNums[n] += 1
            #Start count if n is not present yet
            else:
                hashNums[n] = 1

        final = []
        for i in range(k):
            #Find the number with the highest frequency currently in the dict
            max_key = max(hashNums, key=hashNums.get)
            #Append the most frequent element to the final list
            final.append(max_key)
            #Remove the extracted key so the next iteration finds the next highest frequency
            hashNums.pop(max_key)  

        return final   

        