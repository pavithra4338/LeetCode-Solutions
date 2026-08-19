class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            l.append(sum)
        return l