class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            adj[x].append([y, values[i]])
            adj[y].append([x, 1/values[i]])


        def dfs(src, dst, ans, visit):
            if src not in adj or dst not in adj:
                return -1
            if src==dst:
                return ans

            visit.add(src)
            for nei in adj[src]:
                node, val = nei
                if node not in visit:
                    res =  dfs(node, dst, ans*val, visit)
                    if res!=-1:
                        return res

            return -1

        res=[]
        for u, v in queries:
            res.append(dfs(u, v, 1, set()))


        return res
