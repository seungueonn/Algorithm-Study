from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    
    # 다각형의 가장 바깥쪽 테두리를 만들어야함
    
    maps=[[-1] * 102 for _ in range(102)]
    
    for a,b,c,d in rectangle:
        a *= 2
        b *= 2
        c *= 2
        d *= 2
        
        for i in range(a,c+1): # x좌표
            for j in range(b,d+1): # y좌표
                
                if a < i < c and b < j < d: # 내부
                    maps[i][j] = 0
                elif maps[i][j] == -1: # 테두리
                    maps[i][j] = 1
                    
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    visited=[[0] * 102 for _ in range(102)]
    
    def bfs(x,y):
        
        nonlocal visited
        
        que=deque([(x,y)])
        visited[x][y] = 1
        
        while que:
            x,y=que.popleft()
            
            if x == itemX * 2 and y == itemY * 2:
                return visited[x][y] // 2
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= 102 or ny >= 102:
                    continue
                    
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
                    
        # return 0
    return bfs(characterX * 2, characterY * 2)
    
