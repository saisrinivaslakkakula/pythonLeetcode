class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = path.split('/')
        stack = []
        for d in dir_list:
            #print(d)
            if d !='':
                if d =='..':
                    if stack:stack.pop()
                elif d =='.':
                    continue
                else:
                    stack.append('/'+d)
        if stack: return("".join(stack))
        else: return"/"
                    
            
        