class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            maxi=nums[0]
            mini=nums[i]
            for j in nums[:i+1]:
                if j > maxi:
                    maxi=j
            for j in nums[i:]:
                if j < mini:
                    mini=j
            if maxi-mini<=k:
                return i
        return -1