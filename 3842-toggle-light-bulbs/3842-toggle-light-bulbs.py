class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        l=[]
        for bulb in bulbs:
            if bulbs.count(bulb)%2!=0 and bulb not in l:
                l.append(bulb)
        return sorted(l)