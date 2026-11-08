class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        box=0
        n=sorted(capacity)
        s=sum(apple)
        for i in range(len(n)):
            s-=n[-(i+1)]
            box+=1
            if s<=0:
                break
        return box