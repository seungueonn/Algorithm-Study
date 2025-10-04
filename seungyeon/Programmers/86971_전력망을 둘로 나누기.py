from collections import deque 

def solution(n, wires):
    
    
    answer = n
    
    graph=[[] for _ in range(n+1)]
    
    
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
        
    
    def bfs(start):
        que=deque([start])
        
        visited=[0]*(n+1)
        visited[start] = 1
        
        cnt = 0
        
        while que:
            x = que.popleft()
            
            for i in graph[x]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        
        answer=min(abs(bfs(x)-bfs(y)),answer)
        
        graph[x].append(y)
        graph[y].append(x)
        


    return answer