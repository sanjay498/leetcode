class Solution(object):
    def isValid(self, s):
        a = {"(":")","[":"]","{":"}"}
        open=[]
        for char in s:
            if char in a:
                open.append(char)
            else:
                if not open or a[open.pop()]!=char:
                    return False
        return not open


            
        