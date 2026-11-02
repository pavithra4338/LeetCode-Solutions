class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median=nums[len(nums)//2]
        moves=0
        for i in nums:
            moves+=abs(i-median)
        return moves