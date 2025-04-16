class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right=0
        for num in nums:
            if num !=0:
                nums[right]=num
                right+=1
        while right<len(nums):
            nums[right]=0
            right+=1
        print(nums)
nums=[0,1,0,3,12]
sol=Solution()
sol.moveZeroes(nums)                    