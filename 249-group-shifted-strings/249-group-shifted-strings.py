from collections import defaultdict
class Solution:
    def calculateShiftingSeq(self,string):
        i=1
        res = ""
        while i<len(string):
            shift = ord(string[i]) - ord(string[i-1])
            if shift <0: shift = 26+(shift)
            res+= ","+str(shift)
            i+=1
        return res
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seqMap = {}
        for s in strings:
            shiftSeq = self.calculateShiftingSeq(s)
            if shiftSeq not in seqMap: seqMap[shiftSeq] = [s]
            else: seqMap[shiftSeq].append(s)
        res = []
        for seq in seqMap:
            res.append(seqMap[seq])
        print(seqMap)
        return(res)
            
            
                
                
                    
                
        