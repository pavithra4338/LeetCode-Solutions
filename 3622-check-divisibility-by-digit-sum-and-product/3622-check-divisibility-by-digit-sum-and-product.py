class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        product=1
        for i in str(n):
            sum+=int(i)
            product*=int(i)
        total_sum=sum+product
        if n % total_sum == 0:
            return True
        return False