class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Create an empty map to track the visited values
        initMap = {}

        #Enumerate the values of num in order to get indexes
        for i, val in enumerate(nums):
            #Get the complement number I am looking for 
            complement = target - val  
            if complement in initMap:
                #Return the pair of indexes, return the index already present in the map first
                return [initMap[complement], i]
            else:
                #Add the new value to initMap
                initMap[val] = i
        #Return an empty list if there is no match
        return []
