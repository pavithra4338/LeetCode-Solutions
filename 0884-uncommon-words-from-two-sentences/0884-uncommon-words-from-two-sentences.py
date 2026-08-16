class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        freq={}
        for i in s1.split():
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in s2.split():
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        l=[]
        for word in freq:
            if freq[word]==1:
                l.append(word)
        return l