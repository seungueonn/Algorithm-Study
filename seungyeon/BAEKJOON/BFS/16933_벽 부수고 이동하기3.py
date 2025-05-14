
import sys
from collections import deque

input=sys.stdin.readline

Y,X,K=map(int,input().split())
arr=[]
for _ in range(Y):
    arr.append(list(map(int,input().strip())))

# 처음이동할 때 낮, 한번 이동할 때마다 낮,밤,낮. 이동하지 앟아도 낮과 밤이 바뀜
# 벽은 낮에만 부술 수 있다

dx=[-1,1,0,0]
dy=[0,0,1,-1]

visited=[[[0] * (K+1) for _ in range(X)] for _ in range(Y) ]

def bfs(x,y,z):
    que=deque()
    que.append((x,y,z,1))
    visited[y][x][z] = 1
    

    while que:
        x,y,z,ans=que.popleft()

        is_able_to_move = ans % 2

        if x == X-1 and y == Y-1:
            return ans

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                continue

            if arr[ny][nx] == 0 and visited[ny][nx][z] == 0:
                que.append((nx,ny,z,ans+1))
                visited[ny][nx][z] = ans
            
            if arr[ny][nx] == 1 and z+1 <= K and visited[ny][nx][z+1] == 0:
                if is_able_to_move:
                    visited[ny][nx][z+1] = ans
                    que.append((nx,ny,z+1,ans+1))
                else:
                    que.append((x,y,z,ans+1))

    return -1


print(bfs(0,0,0))
