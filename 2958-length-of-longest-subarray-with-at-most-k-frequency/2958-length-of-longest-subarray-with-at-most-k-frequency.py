class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        left=0
        longest=0
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest
        