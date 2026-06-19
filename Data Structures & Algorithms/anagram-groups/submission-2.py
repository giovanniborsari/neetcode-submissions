class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashA = {}

        for s in strs:
            #Sorts the current string and put it together
            sortedS = "".join(sorted(s))
            if sortedS in hashA:
                #Append the new original word
                hashA[sortedS].append(s)
            else:
                #I have to return a list of strings
                #[s] make it a List[List[str]]
                hashA[sortedS] = [s]
                  
        
        return list(hashA.values())    
        

        