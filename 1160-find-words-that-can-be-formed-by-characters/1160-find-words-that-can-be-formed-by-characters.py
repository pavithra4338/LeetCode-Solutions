class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total=0
        for word in words:
            freq={}
            for ch in chars:
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1
            good=True
            for ch in word:
                if ch not in freq or freq[ch]==0:
                    good = False
                    break
                freq[ch]-=1
            if good:
                total+=len(word)
        return total

