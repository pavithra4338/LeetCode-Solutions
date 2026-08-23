class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi = 0
        for customer in accounts:
            total = 0
            for money in customer:
                total += money
            maxi = max(maxi, total)
        return maxi