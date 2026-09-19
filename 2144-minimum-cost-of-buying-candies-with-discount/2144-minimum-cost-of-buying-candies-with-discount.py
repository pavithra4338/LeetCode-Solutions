class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        choose=0
        minimum=0
        for i in range(len(cost)-1,-1,-1):
            if choose==2:
                choose=0
            else:
                minimum+=cost[i]
                choose+=1
        return minimum