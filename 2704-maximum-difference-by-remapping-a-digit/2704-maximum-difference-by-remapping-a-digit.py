class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)
        max_digit = ''
        for ch in s:
            if ch != '9':
                max_digit = ch
                break
        max_num = s.replace(max_digit, '9') if max_digit else s

        min_digit = s[0]
        min_num = s.replace(min_digit, '0')
        
        return int(max_num) - int(min_num)
