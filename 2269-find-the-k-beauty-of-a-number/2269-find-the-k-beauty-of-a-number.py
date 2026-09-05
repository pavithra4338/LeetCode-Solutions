class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        nums=str(num)
        c=0
        for i in range(len(nums)-k+1):
            sub=int(nums[i:i+k])
            if sub != 0 and num % sub ==0:
                c+=1
        return c