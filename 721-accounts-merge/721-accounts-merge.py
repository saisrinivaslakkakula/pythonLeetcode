class Solution(object):
    # Read notes
    def DFS(self,email,graph,visited,nodes):
        nodes.append(email)
        visited.add(email)
        for neighbor in graph[email]:
            if neighbor not in visited:
                self.DFS(neighbor,graph,visited,nodes)
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = defaultdict(list)
        acc_map = {}
        visited = set()
        for account_list in accounts:
            account_name = account_list[0]
            acc_first_email = account_list[1]
            acc_rest_emails = account_list[2:]
            for rest in acc_rest_emails:
                graph.setdefault(rest, set()).add(acc_first_email)
                graph.setdefault(acc_first_email, set()).add(rest)
            acc_map[acc_first_email] = account_name # name
        res = []
        emails = acc_map.keys()
        emails.sort()
        for email in emails:
            acc = acc_map[email]
            nodes = []
            if email not in visited:
                #print("Here",graph[email])
                self.DFS(email,graph,visited,nodes)
                nodes.sort()
                nodes = [acc]+nodes
                #nodes = [acc]+nodes
            if email not in graph:
                #print("Here",email)
                nodes.append(acc)
                nodes.append(email)
            if nodes:res.append(nodes)
        return(res)
                
                
        
                
            