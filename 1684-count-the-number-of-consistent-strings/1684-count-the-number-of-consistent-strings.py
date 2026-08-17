class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for word in words:
            consist=True
            for ch in word:
                if ch not in allowed:
                    consist=False
                    break
            if consist:
                c+=1
        return c