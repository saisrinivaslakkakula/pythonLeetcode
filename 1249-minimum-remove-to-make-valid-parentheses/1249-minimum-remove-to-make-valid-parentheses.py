class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i,c in enumerate(s):
            if c =="(": stack.append(('(',i))
            elif c==")":
                if len(stack)>0 and stack[-1][0] =='(': stack.pop()
                else: stack.append((')',i))
        #print(stack)
        str_list = list(s)
        for c in stack:
            char,idx = c
            str_list[idx] = ""
        return "".join(str_list)
            
                    
        