class Solution(object):
    def permute(self, nums):
        result = []

        def run(start):
            if start >= len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]   # choose
                run(start + 1)                                # next slot
                nums[i], nums[start] = nums[start], nums[i]   # undo

        run(0)
        return result