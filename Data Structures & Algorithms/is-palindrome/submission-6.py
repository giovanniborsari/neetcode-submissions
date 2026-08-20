class Solution:
    def isPalindrome(self, s: str) -> bool:
        #converts s to lower case
        s = s.lower()

        newStr = ""
        for c in s:
            #check if c is alphanumeric
            if c.isalnum():
                #append c to the end of string
                newStr += c
        
        #Compare newStr with its reversed version
        return newStr == (newStr[::-1])