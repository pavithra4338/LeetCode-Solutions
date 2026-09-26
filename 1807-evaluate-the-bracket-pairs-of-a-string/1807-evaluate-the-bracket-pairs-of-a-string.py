class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        freq={}
        for i in range(len(knowledge)):
            freq[knowledge[i][0]]=knowledge[i][1]
        s=re.split(r"[()]",s)
        for i in range(1,len(s),2):
            if s[i] in freq:
                s[i]=freq[s[i]]
            else:
                s[i]="?"
        return "".join(s)