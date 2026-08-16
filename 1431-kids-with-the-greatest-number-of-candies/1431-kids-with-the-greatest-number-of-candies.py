class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l=[]
        great = max(candies)
        for i in candies:
            l.append((i + extraCandies) >= great)
        return l