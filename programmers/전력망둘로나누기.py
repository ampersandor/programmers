def dfs(cur, nodes, visited):
    if visited[cur]:
        return 0
    visited[cur] = True
    num_nodes = 1
    for child in nodes[cur]:
        num_nodes += dfs(child, nodes, visited)
    return num_nodes

def solution(n, wires):
    answer = 100
    nodes = [[] for _ in range(n + 1)]
    for a, b in wires:
        nodes[a].append(b)
        nodes[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n + 1)
        visited[b] = True
        num_nodes_a = dfs(a, nodes, visited)
        num_nodes_b = n - num_nodes_a        
        answer = min(answer, abs(num_nodes_a - num_nodes_b))
        
            
    return answer