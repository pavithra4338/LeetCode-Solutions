class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        s="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            if i not in sentence:
                return False
        return True
