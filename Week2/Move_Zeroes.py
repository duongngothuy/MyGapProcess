class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = 0 #for non zero ele
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1] = nums[i]
                p1 += 1
        for i in range(p1, len(nums)): #for the rest where all 0s
            nums[i] = 0
        
            

        