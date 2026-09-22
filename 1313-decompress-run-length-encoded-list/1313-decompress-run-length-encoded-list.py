class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(0,len(nums)-1,2):
            l.extend([nums[i+1]]*nums[i])
        return l