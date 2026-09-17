class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}
        for ind,num in enumerate(nums):
            temp=target-num
            if temp in freq:
                return ([freq[temp],ind])
                break
            else:
                freq[num]=ind
       
