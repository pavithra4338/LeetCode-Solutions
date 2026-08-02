class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                n=nums.index(target)
            else:
                nums.append(target)
                nums.sort()
                n=nums.index(target)
        return n
        