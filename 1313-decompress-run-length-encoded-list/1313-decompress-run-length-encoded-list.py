class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(0,len(nums)-1,2):
            freq=nums[i]
            value=nums[i+1]
            for j in range(freq):
                l.append(value)
        return l