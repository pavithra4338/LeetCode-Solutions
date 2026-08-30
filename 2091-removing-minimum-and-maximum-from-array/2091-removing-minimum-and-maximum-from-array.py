class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))
        left = min(mini, maxi)
        right = max(mini, maxi)
        front = right + 1
        back = len(nums) - left
        both = (left + 1) + (len(nums) - right)
        return min(front, back, both)