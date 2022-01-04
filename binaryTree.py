from binarytree import build
from collections import deque

class solution:
    def inorderTraversal(self,root,badstudents) -> int:
        if not root: return []
        stack = []
        curr = root
        res = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if curr.value not in badstudents: res.append(curr.val)
                curr = curr.right
        return (res)
    def helper(self,node, level,levels,firstbech):
        if len(levels) == level: levels.append([])
        if node:
            if node.value not in firstbech :levels[level].append(node)
        if node.left: self.helper(node.left, level + 1,levels,firstbech)
        if node.right: self.helper(node.right, level + 1,levels,firstbech)


    def calculateCheatWays(self)->int:
        nodes = [1, 2, 8, 3, 4, 9, 10, None, None, 5, 6, None, None, None, None, None, None, None, None, None, None, 7]
        root = build(nodes)
        levels = []
        firstbech = set()
        firstbech.add(1)
        firstbech.add(2)
        self.helper(root, 0,levels,firstbech)
        print(levels)
        badstudents = [item for sublist in levels for item in sublist]
        maximum = 0
        for bad in badstudents:
            #pass
            curcount = self.inorderTraversal(bad,badstudents)
            #if len(curcount)> maximum: maximum = curcount

        return(maximum)




sol = solution()
print(sol.calculateCheatWays())

