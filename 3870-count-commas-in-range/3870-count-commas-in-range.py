class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n))<4:
            return 0
        total=0
        for i in range(1000,n+1):
            total+=1
        return total