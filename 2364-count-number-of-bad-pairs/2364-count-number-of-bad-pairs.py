class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        good = 0
        for i in range(len(nums)):
            x = i - nums[i]
            if x in freq:
                good += freq[x]
                freq[x] += 1
            else:
                freq[x] = 1
        total = len(nums) * (len(nums) - 1) // 2
        return total - good