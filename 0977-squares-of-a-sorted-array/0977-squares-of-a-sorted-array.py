class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for num in nums:
            l.append(num**2)
        l.sort()
        return l 