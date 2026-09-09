class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        c=0
        start=1000
        while start <= n:
            c += n-start+1
            start*=1000
        return c