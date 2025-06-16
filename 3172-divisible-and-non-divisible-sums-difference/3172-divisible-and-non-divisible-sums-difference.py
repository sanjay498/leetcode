class Solution(object):
    def differenceOfSums(self, n, m):
        div=0
        ndiv=0
        for i in  range(1,1+n):
            if i%m==0:
                div+=i
            else:
                ndiv+=i
        su=ndiv-div
        return su           
                  
