class Solution:

    def encode(self, strs: List[str]) -> str:
        #Marks start and end of an element
        encode = "#;"

        for s in strs:
            #append the next encoded element to string
            encode = encode + s + "#;"

        return encode

    def decode(self, s: str) -> List[str]:

        firstIndex = ""
        secondIndex = ""
        decoded = []
        for c in s:
            #Check for empty string
            if (s == "#;") :
                break
            #Find first ocurrence of #;
            firstIndex = s.find("#;")
            #Get a substring after first index
            s = s[(firstIndex)+2:]
            secondIndex = s.find("#;")
            decoded.append(s[:secondIndex])
            s = s[secondIndex:]
            
        
        return(decoded)
                

