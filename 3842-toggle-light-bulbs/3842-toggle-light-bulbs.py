class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        l=[]
        for bulb in bulbs:
            if bulb in l:
                l.remove(bulb)
            else:
                l.append(bulb)
        return sorted(l)