class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr1=sorted(arr)
        rank=1
        freq={}
        for i in arr1:
            if i not in freq:
                freq[i]=rank
                rank+=1
        return [freq[i] for i in arr]