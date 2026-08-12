class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n=max(nums)
        l=[]
        for i in range(1,n+1):
            l.append(i)
        l.append(n)
        return nums == l
