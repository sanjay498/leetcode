class Solution(object):
    def longestPalindrome(self, s):
        max_pal=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                if sub==sub[::-1] and len(sub)>len(max_pal):
                    max_pal=sub
        return max_pal            
            

        