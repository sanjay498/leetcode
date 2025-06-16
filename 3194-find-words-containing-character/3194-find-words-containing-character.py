class Solution(object):
    def findWordsContaining(self, words, x):
        a=[]
        for i,word in enumerate(words):
            for ch in word:
                if ch==x:
                    a.append(i)
                    break
        return a
        