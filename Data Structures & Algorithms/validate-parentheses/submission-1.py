class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # create empty stack
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # hash stores matches

        for c in s:
            if c in closeToOpen: # if closing symbol
                # if top item in stack = matching opening symbol
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # remove from stack
                else:
                    return False # if latest not matching then false
            else:
                stack.append(c) # if not closing symbol simply just add to stack
                 
        # all opening symbols should be added then popped from stack     
        return True if not stack else False