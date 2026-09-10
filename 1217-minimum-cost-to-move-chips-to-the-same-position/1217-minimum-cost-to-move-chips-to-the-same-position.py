class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even=0
        odd=0
        for i in range(len(position)):
            if position[i]%2==0:
                even+=1
            else:
                odd+=1
        return min(even,odd)