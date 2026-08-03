class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}
        l=[]
        for i in nums1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in nums2:
            if i in freq and i not in l:
                l.append(i) 
        return l

        