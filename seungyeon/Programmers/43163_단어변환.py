from collections import deque

def solution(begin, target, words):
    answer = 0
    
    def bfs(x):
        
        nonlocal answer
        
        que=deque([(x,0)])
        
        visited=[]
        visited.append(x)
        
        while que:
            x,step = que.popleft()
            
            if x == target:
                return step
            
            for word in words:
                if word not in visited:
                    
                    cnt = 0
                    for i in range(len(word)):
                        if word[i] != x[i]:
                            cnt += 1
                            
                    if cnt == 1:
                        que.append((word,step+1))
    
    if target not in words:
        return 0
    
    return bfs(begin)
