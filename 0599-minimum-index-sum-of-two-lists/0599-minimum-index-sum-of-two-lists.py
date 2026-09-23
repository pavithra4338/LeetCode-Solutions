class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l=[]
        mini=float('inf')
        for i,ele in enumerate(list1):
            if ele in list2:
                temp=i+list2.index(ele)
                if temp<mini:
                    mini=temp
                    l=[ele]
                elif temp==mini:
                    l.append(ele)
        return l

