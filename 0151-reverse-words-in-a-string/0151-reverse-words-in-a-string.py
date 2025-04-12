class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        reversed_word=' '.join(reversed(word))
        return reversed_word
sol=Solution()

sol.reverseWords("the sky is blue")
sol.reverseWords(" hello world  ")
sol.reverseWords("a good   example")  