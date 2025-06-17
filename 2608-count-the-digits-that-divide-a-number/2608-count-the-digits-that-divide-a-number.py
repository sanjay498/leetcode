class Solution(object):
    def countDigits(self, num):
        k = num
        count = 0

        while k > 0:
            digit = k % 10     
            if digit != 0 and num % digit == 0:
                count += 1
            k = k // 10        
        return count
