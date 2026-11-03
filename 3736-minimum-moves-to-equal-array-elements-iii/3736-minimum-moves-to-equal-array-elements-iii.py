class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=max(nums)
        moves=0
        for i in nums:
            moves+=maximum-i
        return moves
