class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        for i,c in enumerate(s):
            if c =='(':
                stack.append(i)
            elif c ==')' and stack:
                stack.pop()
            elif c ==')' and not stack:
                indices_to_remove.add(i)
        indices_to_remove = indices_to_remove.union(set(stack))
        res_list = []
        for i,c in enumerate(s):
            if i not in indices_to_remove:
                res_list.append(c)
        res = "".join(res_list)
        return(res)
        
                
        