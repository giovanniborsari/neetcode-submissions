class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #If len is different they cannot be an anagram
        if len(s) != len(t):
            return False
        #Sort both strings
        sortedS = sorted(s)
        sortedT = sorted(t)
        #Iterate through all the indexes
        for i in range(len(s)):
            #If the value is not the same return false
            if sortedS[i] != sortedT[i]:
                return False
        #If the code reaches here they are anagrams
        return True       
            

