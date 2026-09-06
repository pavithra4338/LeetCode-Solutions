class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        c=0
        k=3
        freq={}
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1

            if r-l == k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    freq.pop(s[l])
                l+=1
            if len(freq) == k:
                c+=1
        return c