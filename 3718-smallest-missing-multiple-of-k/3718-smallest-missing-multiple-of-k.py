class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = k
        while True:
            if i not in nums:
                return i
            i += k