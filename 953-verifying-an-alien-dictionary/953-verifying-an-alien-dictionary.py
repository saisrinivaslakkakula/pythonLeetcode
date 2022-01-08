class Solution:
    def helper(self,word1,word2,order_d)->bool:
        min_i = min(len(word1),len(word2))
        i=0
        while i<min_i:
            if order_d[word2[i]]<order_d[word1[i]]:return False
            elif order_d[word2[i]]>order_d[word1[i]]: return True
            else:i+=1
        if len(word1) <= len(word2):return True
        else: return False
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1: return True
        order_d = {}
        for i,c in enumerate(order):order_d[c] =i
        for i in range(len(words)-1):
            if not self.helper(words[i],words[i+1],order_d):return False
        return True
        