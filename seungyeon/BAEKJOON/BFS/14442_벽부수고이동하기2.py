# 최단경로, 시작, 끝나는 칸도 포함해서 센다

import sys
from collections import deque
input=sys.stdin.readline
Y,X,K=map(int,input().split())

arr=[]
for _ in range(Y):
    arr.append(list(map(int,input().strip())))


visited=[ [[0]*(K+1) for _ in range(X)] for _ in range(Y)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,z):

    que=deque()
    que.append([x,y,z])
    visited[y][x][z] = 1

    while que:
        x,y,z=que.popleft()
        
        if x == X-1 and y == Y-1:
            return visited[y][x][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                continue

            if arr[ny][nx] == 0 and visited[ny][nx][z] == 0:
                visited[ny][nx][z] = visited[y][x][z] + 1
                que.append([nx,ny,z])

            if arr[ny][nx] == 1 and z+1 <= K and visited[ny][nx][z+1]== 0 :
                visited[ny][nx][z+1] = visited[y][x][z] + 1
                que.append([nx,ny,z+1])

    return -1

print(bfs(0,0,0))