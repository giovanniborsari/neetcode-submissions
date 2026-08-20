class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        #If s has an odd number of characters return False
        if (len(s)%2) == 1:
            return False

        #If starts with a closing symbol returns False
        if s[0] == "]" or s[0] == ")" or s[0] == "}":
            return False

        for c in s:
            #Look for an opening symbol if spots a closing symbol
            if c == "}" and len(stack) > 0:
                closing = stack.pop()
                if closing != "{":
                    return False
            elif c == ")" and len(stack) > 0:
                closing = stack.pop()
                if closing != "(":
                    return False
            elif c == "]" and len(stack) > 0:
                closing = stack.pop()
                if closing != "[":
                    return False
            else:
                #Append opening symbols to stack
                stack.append(c)

        #Check if some symbols were not closed
        if len(stack) != 0:
            return False

        return True
