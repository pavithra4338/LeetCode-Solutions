class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate=0
        for num in nums:
            if nums.count(num)==2:
                duplicate=num
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                return [duplicate,i]
