class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            maxi=max(nums[:i+1])
            mini=min(nums[i:])
            if maxi-mini<=k:
                return i
        return -1