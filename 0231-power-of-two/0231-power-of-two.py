class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        valid=False
        if n>0 and n&(n-1)==0:
            valid=True
        return valid