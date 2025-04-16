import math
class Solution:
    def gcdOfStrings(self,str1,str2):
        if str1+str2!=str2+str1:
            return ""
        length=math.gcd(len(str1),len(str2))
        return str1[:length] 
sol=Solution()        
str1 = "ABCABC"
str2 = "ABC"
result=sol.gcdOfStrings(str1,str2)
print(result)

        