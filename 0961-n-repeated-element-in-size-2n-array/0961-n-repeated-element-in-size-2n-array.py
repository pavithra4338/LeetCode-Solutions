class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in nums:
            if i in freq:
                return i
            else:
                freq[i]=1
        return
        