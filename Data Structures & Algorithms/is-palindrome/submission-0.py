class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.strip().casefold()

        newStr = ""
        for c in string:
            if (c.isalnum() and not c.isspace()):
                newStr += c
        
        return newStr == (newStr[::-1])