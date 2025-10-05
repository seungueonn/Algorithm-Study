from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

    
def solution(maps):
    answer = 0
    
    n,m=len(maps),len(maps[0])
    
    visited=[[-1] * m for _ in range(n)]
    
    
    def bfs(x,y):

        que=deque([(x,y)])
        visited[x][y] = 1

        while que:
            x,y=que.popleft()

            if x == n-1 and y == m-1:
                return visited[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue


                if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
        
        print(visited)
        return -1

    answer = bfs(0,0)

    return answer