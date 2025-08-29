from collections import deque

def solution(storage, requests):
    
    h = len(storage)+2
    w = len(storage[0])+2
    
    
    arr=[['-'] * w for _ in range(h)]
    
        
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    
    def bfs():
        
        visited=[[False]*w for _ in range(h)]
        que=deque()
        que.append((0,0))
        visited[0][0] = True
        
        while que:
            x,y=que.popleft()
        
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    
                    if arr[nx][ny] == '-':
                        que.append((nx,ny))
                        visited[nx][ny] = True
                    elif arr[nx][ny] == '1':
                        visited[nx][ny] = True
                        que.append((nx,ny))
                        arr[nx][ny] = '-'
                    
    for i in range(1,h-1):
        for j in range(1,w-1):
            arr[i][j] = storage[i-1][j-1]
            
    for request in requests:
        if len(request) == 1: # 지게차
            tmp = []
            target = request[0]
            
            for i in range(1,h-1):
                for j in range(1,w-1):
                    if arr[i][j] == target:
                        for k in range(4):
                            nx = i + dx[k]
                            ny = j + dy[k]
                            
                            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '-':
                                tmp.append((i,j))
                                break
                                
            for ti,tj in tmp:
                arr[ti][tj] = '-'

            bfs()
        else:
            target = request[0]

            for i in range(1,h-1):
                for j in range(1,w-1):
                    if arr[i][j] == target:
                        arr[i][j] = '1'

            bfs()
        
        
    answer=0
    for i in range(1,h-1):
        for j in range(1,w-1):
            if arr[i][j] != '-' and arr[i][j] != '1':
                answer += 1
    
    
            
    return answer