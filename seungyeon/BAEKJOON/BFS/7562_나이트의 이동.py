# import sys
# from collections import deque
# input=sys.stdin.readline


    
# def bfs(x,y):


#     dx = [-1, 1, 2, 2, 1, -1, -2, -2]
#     dy = [2, 2, 1, -1, -2, -2, -1, 1]

#     que = deque()

#     que.append((x,y))


#     while(que):
#         x,y = que.popleft()

#         if x == goalX and y == goalY:
#             return arr[x][y] 

#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= k or ny < 0 or ny >= k:
#                 continue

#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = arr[x][y] + 1 
#                 que.append((nx,ny))


# t =int(input())

# for i in range(t):
#     k = int(input())
#     currX,currY = map(int,input().split())
#     goalX,goalY = map(int,input().split())
#     arr = [[0]*k for _ in range(k)]
#     print(bfs(currX,currY))




import sys
from collections import deque

input=sys.stdin.readline

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs(a,b,c,d):

    que=deque()
    que.append((a,b))

    while que:
        x,y=que.popleft()

        if x == c and y == d:
            return arr[y][x]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if arr[ny][nx] == 0 :#not visited[ny][nx]:
                arr[ny][nx] = arr[y][x] + 1
                que.append((nx,ny))
                
    return 0

t=int(input())


for i in range(t):
    n=int(input())

    arr=[[0]* n for _ in range(n)]
    # visited=[[False]]
    a,b=map(int,input().split())
    c,d=map(int,input().split())

    print(bfs(a,b,c,d))


