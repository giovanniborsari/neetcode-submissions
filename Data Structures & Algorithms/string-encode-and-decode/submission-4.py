class Solution:

    def encode(self, strs: List[str]) -> str:
    
        encode = "#;"

        for s in strs:
            encode = encode + s + "#;"

        return encode

    def decode(self, s: str) -> List[str]:

        firstIndex = ""
        secondIndex = ""
        decoded = []
        for c in s:
            if (s == "#;") :
                break
            firstIndex = s.find("#;")
            if firstIndex >= len(s):
                break
            s = s[(firstIndex)+2:]
            secondIndex = s.find("#;")
            if secondIndex >= len(s):
                break
            decoded.append(s[:secondIndex])
            s = s[secondIndex:]
            
        
        return(decoded)
                

