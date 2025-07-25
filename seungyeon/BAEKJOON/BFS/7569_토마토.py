

# # # import sys
# # # X,Y,H=map(int,input().split())
# # # arr=[[] for _ in range(H)]
# # # for i in range(H):
# # #     for j in range(Y):
# # #         arr[i].append(list(map(int,input().split())))


# # # dx=[-1,1,0,0,0,0]
# # # dy=[0,0,1,-1,0,0]
# # # dh=[0,0,0,0,-1,1]

# # # visited=[[[False for _ in range(X)] for _ in range(Y)] for _ in range(H)]
# # # from collections import deque

# # # que=deque()
# # # answer = 0

# # # def bfs():

# # #     while que:
# # #         h,y,x=que.popleft()

# # #         for k in range(6):
# # #             nh=h+dh[k]
# # #             nx=x+dx[k]
# # #             ny=y+dy[k]

# # #             if nx < 0 or ny < 0 or nh < 0 or nx >= X or ny >= Y or nh >= H:
# # #                 continue

# # #             if arr[nh][ny][nx] == 0 and not visited[nh][ny][nx]:
# # #                 que.append(((nh,ny,nx)))
# # #                 arr[nh][ny][nx] = arr[h][y][x] + 1
# # #                 visited[nh][ny][nx] = True

# # # for h in range(H):
# # #     for j in range(Y):
# # #         for i in range(X):
# # #             if not visited[h][j][i] and arr[h][j][i] == 1:
# # #                 que.append((h,j,i))
# # #                 visited[h][j][i] = True

# # # bfs()

# # # for a in arr:
# # #     for b in a:
# # #         for c in b:
# # #             if c == 0:
# # #                 print(-1)
# # #                 exit(0)

# # #         answer = max(answer,max(b))

# # # print(answer -1)
                    


# # import sys
# # from collections import deque

# # X,Y,H=map(int,input().split())

# # arr=[[ ] for _ in range(H)]
# # for h in range(H):
# #     for j in range(Y):
# #         arr[h].append(list(map(int,input().split())))


# # dx=[-1,1,0,0,0,0]
# # dy=[0,0,1,-1,0,0]
# # dh=[0,0,0,0,-1,1]

# # que = deque()

# # visited=[[[False for _ in range(X)] for _ in range(Y)] for _ in range(H)]
# # def bfs():


# #     while que:
# #         h,y,x=que.popleft()

# #         for i in range(6):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #             nh = h + dh[i]


# #             if nx < 0 or ny < 0 or nh < 0 or nx >= X or ny >= Y or nh >= H:
# #                 continue

# #             if arr[nh][ny][nx] == 0 and not visited[nh][ny][nx]:
# #                 que.append((nh,ny,nx))
# #                 arr[nh][ny][nx] = arr[h][y][x] + 1
# #                 visited[nh][ny][nx] = True



# # answer = 0
# # for i in range(H):
# #     for j in range(Y):
# #         for k in range(X):

# #             if arr[i][j][k] == 1 and not visited[i][j][k]:
# #                 que.append((i,j,k))


# # bfs()


# # for i in arr:
# #     for j in i:
# #         for k in j:
# #             if k == 0:
# #                 print(-1)
# #                 exit(0)

# #         answer = max(answer,max(j))

# # print(answer -1)

# import sys
# from collections import deque

# input=sys.stdin.readline

# X,Y=map(int,input().split())
# arr=[]
# is_able=False
# que=deque()
# for i in range(Y):
#     input_sub = list(map(int,input().split()))
#     arr.append(input_sub)
    
#     for j in range(X):
#         if input_sub[j] == 1:
#             que.append((j,i))
#             is_able=True


# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# def bfs():

#     while que:
#         x,y=que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= X or ny >= Y:
#                 continue

#             if arr[ny][nx] < 0 : # 토마토 없음
#                 continue

#             if arr[ny][nx] == 0 :
#                 arr[ny][nx] = arr[y][x] + 1
#                 que.append((nx,ny))

#     answer=0
#     for a in arr:
#         for j in a:
#             if j == 0:
#                 print(-1)
#                 return 
#             else:
#                 answer=max(answer,max(a))

#     print(answer-1)

# if not is_able:
#     print(0)
# else:
#     bfs()


import sys
from collections import deque

input=sys.stdin.readline

m,n=map(int,input().split()) # 가로 , 세로 

arr=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]

visited=[[False]*m for _ in range(n)]


for i in range(n):
    arr.append(list(map(int,input().split())))


# 1을 발견하면 bfs
def bfs():

    while que:

        x,y=que.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = True
                que.append((nx,ny))


que=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            que.append((i,j))

bfs()

answer=0
check=False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            check=True
            
    answer=max(answer,max(arr[i]))

if check:
    print(-1)
else:
    print(answer-1)