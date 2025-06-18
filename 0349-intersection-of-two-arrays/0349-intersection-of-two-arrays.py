import numpy as np

class Solution(object):
    def intersection(self, nums1, nums2):
        k = []
        for num in nums1:
            if num in nums2 and num not in k:
                k.append(num)
        
        arr = np.array(k)
        return arr.tolist()