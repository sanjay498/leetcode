class Solution:
    
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while right > left and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
sol=Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))
