import itertools
from itertools import product
class Solution:
    def generateCombinations(self,l1,l2)->List[str]:
        #print(l1)
        unique_combinations = []
        unique_combinations = [ ""+x+y+"" for x in l1 for y in l2]
        #print(unique_combinations)
        return(unique_combinations)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <=0: return []
        
        letters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits) == 1: return letters[digits]
        temp = []
        for digit in digits:
            temp.append(letters[digit])
        #print(temp)
        res = []
        res.append(temp[0])
        #print(res)
        for i in range(1,len(temp)):
            #print("Tmp[i]",temp[i])
            #print("lastres",res[-1])
            res.append(self.generateCombinations(res[-1],temp[i]))
            #print(res)
        print(res[-1])
        return(res[-1])
        