from collections import deque

def bfs(visited,graph,start):
    
    que=deque([(start)])
    
    visited[start] = 1

    
    while que:
        x = que.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                que.append(i)
                
def solution(n, edge):
    answer = 0
    # 1번 노드로 부터 가장 멀리 떨어진 노드 개수 
    
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited=[0] * (n+1)
    
    bfs(visited,graph,1)
    
    max_num = max(visited)
    answer = visited.count(max_num)
    
    return answer