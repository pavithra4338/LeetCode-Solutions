class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq={}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        l=[]
        for i in range(k):
            maximum = max(freq.values())
            selected = ""
            for word in freq:
                if freq[word] == maximum:
                    if selected == "" or word < selected:
                        selected = word
            l.append(selected)
            del freq[selected]
        return l