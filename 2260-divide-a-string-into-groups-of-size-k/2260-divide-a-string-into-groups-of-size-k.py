class Solution(object):
    def divideString(self, s, k, fill):
        l = []
        for i in range(0, len(s), k):
            part = s[i:i + k]
            if len(part) < k:
                part += fill * (k - len(part))
            l.append(part)
        return l
