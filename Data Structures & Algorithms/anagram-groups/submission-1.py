class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashA = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in hashA:
                hashA[sortedS].append(s)
            else:
                hashA[sortedS] = [s]
                  
        
        return list(hashA.values())    
        

        