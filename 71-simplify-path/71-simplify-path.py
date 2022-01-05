class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split("/")
        stack = []
        for name in split:
            if name ==".":continue
            if name !="" and name !="..":
                stack.append("/"+name)
            if name ==".." and stack:
                stack.pop()
        path = "".join(stack)
        if path != "": return path
        else: return "/"
        
                
        