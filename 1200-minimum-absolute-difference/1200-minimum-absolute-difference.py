class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff=float("inf")
        for i in range(1,len(arr)):
            diff = arr[i]-arr[i-1]
            min_diff = min(min_diff,diff)
        l=[]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                l.append([arr[i - 1], arr[i]])
        return l