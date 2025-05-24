# import sys
# from collections import deque
# input=sys.stdin.readline
#
#
# dx=[-1,1,0,0,0,0]
# dy=[0,0,1,-1,0,0]
# dh=[0,0,0,0,1,-1]
# def bfs(x,y,h):
#
#     que=deque()
#     que.append((x,y,h))
#     visited[h][y][x] = 1
#
#
#     while que:
#
#         x,y,h=que.popleft()
#
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nh = h + dh[i]
#
#             if nx < 0 or ny < 0 or nh < 0 or nx >= X or ny >= Y or nh >=H:
#                 continue
#
#             if arr[nh][ny][nx] == "." and visited[nh][ny][nx] == 0:
#                 visited[nh][ny][nx] = visited[h][y][x] + 1
#                 que.append((nx,ny,nh))
#
#             if arr[nh][ny][nx] == 'E':
#                 return visited[h][y][x]
#
#
#     return -1
#
#
#
# while True:
#     H,Y,X=map(int,input().split())
#
#     if H==0 and X == 0 and Y == 0:
#         break
#
#     arr=[[] for _ in range(H)]
#     visited=[ [[0] * X for _ in range(Y)] for _ in range(H)]
#     start=(0,0,0)
#     for i in range(H):
#         for j in range(Y):
#             building= list(map(str,input().strip()))
#             arr[i].append(building)
#             for k in range(X):
#                 if building[k] == 'S':
#                     start = (k,j,i) # x,y
#
#         input()
#
#     x,y,h=start
#     result = bfs(x,y,h)
#
#     if result < 0:
#         print("Trapped!")
#     else:
#         print("Escaped in",result,"minute(s).")


import sys
from collections import deque
input=sys.stdin.readline


dh=[0,0,0,0,1,-1]
dx=[-1,1,0,0,0,0]
dy=[0,0,1,-1,0,0]


def bfs(x,y,h):

    que=deque()
    que.append((x,y,h))
    visited[h][y][x] = 0
    while que:
        x,y,h=que.popleft()

        if arr[h][y][x] == 'E':
            print("Escaped in",visited[h][y][x],"minute(s).")
            return

        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or nh < 0 or nx >=X or ny >= Y or nh >= L:
                continue

            if arr[nh][ny][nx] == '#':
                continue

            if visited[nh][ny][nx] == 0:
                visited[nh][ny][nx] = visited[h][y][x] + 1
                que.append((nx,ny,nh))


    print("Trapped!")



while True:
    L,Y,X=map(int,input().split())

    visited = [[[0] * X for _ in range(Y) ]for _ in range(L)]

    if L == 0 and Y == 0 and X == 0:
        break

    arr=[]
    start=(0,0,0)

    for k in range(L):
        floor = [list(map(str,input().strip())) for _ in range(Y)]
        arr.append(floor)

        for i in range(Y):
            for j in range(X):
                if floor[i][j] == 'S':
                    start=(j,i,k)

        input()

    x,y,h=start
    bfs(x,y,h)

