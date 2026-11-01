class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small=min(nums)
        total=sum(nums)
        return total-(len(nums)*small)