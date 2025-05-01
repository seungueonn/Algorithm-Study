# # import sys
# # input=sys.stdin.readline
# # dr=[-1,0,1,0]
# # dc=[0,1,0,-1]

# # n,m=map(int,input().split())
# # r,c,d=map(int,input().split())
# # arr=[list(map(int,input().split())) for _ in range(n)]

# # visited=[[0] * m for _ in range(n)]
# # visited[r][c] = 1 # 출발지

# # answer = 1
# # while True:
# #     check = False

# #     for i in range(4):
# #         d = (d + 3)  % 4

# #         nr = r + dr[d]
# #         nc = c + dc[d]

# #         if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
# #             if visited[nr][nc] == 0:
# #                 visited[nr][nc] = 1
# #                 check = True
# #                 answer += 1
# #                 r = nr
# #                 c = nc
# #                 break

# #     if not check:

# #         if arr[r-dr[d]][c-dc[d]] == 1:
# #             print(answer)
# #             break
# #         else:
# #             r,c = r-dr[d],c-dc[d]


# # # import sys
# # # input=sys.stdin.readline
# # # from collections import deque

# # # n,m=map(int,input().split())
# # # r,c,d=map(int,input().split())
# # # arr=[]

# # # for i in range(n):
# # #     arr.append(list(map(int,input().split())))

# # # dx=[-1,1,0,0]
# # # dy=[0,0,-1,1]

# # # compass = [[0,1],[1,0],[0,-1],[-1,0]]
# # # direct=[[1,0],[0,1],[-1,0],[0,-1]]

# # # def dfs():

# # #     answer =0

# # #     que = deque()
# # #     que.append((r,c))
# # #     while que:
# # #         x,y=que.popleft()

# # #         check=False
        
# # #         for i in range(4):
# # #             nx = x+dx[i]
# # #             ny = y+dy[i]

# # #             if 0 > nx or nx > n or 0 > ny or ny >  m:
# # #                 print(nx,ny,'here??')
# # #                 continue

# # #             if (0 <= nx < n) and (0 <= ny < m) and arr[nx][ny] == 1: # 주변에 청소되지 않은 칸이 있는경우
# # #                 print("here")
# # #                 que.append((nx,ny))
# # #                 arr[nx][ny] = 0
# # #                 answer += 1
# # #                 check=True

# # #         if not check:
# # #             print("hihi")
# # #             x+=compass[d][0]
# # #             y+=compass[d][1]
# # #             que.append((x,y))
        
# # #     return answer
            
# # # print(dfs())




# import sys
# from collections import deque

# input=sys.stdin.readline

# Y,X=map(int,input().split())

# r,c,d=map(int,input().split())

# #북0동1남2서3

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]


# arr=[]
# for i in range(Y):
#     arr.append(list(map(int,input().split())))


# def dfs(x,y,d):

#     que=deque()

#     que.append((x,y,d))
#     while que:

#         x,y,d=que.popleft()

#         arr[y][x] = 1
#         check = True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= X or ny >=Y:
#                 continue

#             if arr[ny][nx] == 0: # 청소 가능
#                 d = (d + 3 - i) % 4 # 반시계 회전
#                 check = False
#                 que.append((nx,ny,d))

#                 arr[ny][nx] += arr[y][x]


#         if check: # 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
#             nx = x - dx[d] # 뒤로가기 
#             ny = y - dy[d]


#             if nx < 0 or ny < 0 or nx >= X or ny >=Y:
#                 # 작동 중지 
#                 break
#             else:
#                 que.append((nx,ny,d))
#                 # 여기서 다시 작동 


# dfs(r,c,d)
# answer = 0
# for i in range(Y):
#     answer = max(answer,max(arr[i]))

# print(answer)


import sys
from collections import deque

input = sys.stdin.readline

Y, X = map(int, input().split())
r, c, d = map(int, input().split())

# 북0 동1 남2 서3
dx = [-1, 0, 1, 0]  # 위, 오, 아래, 왼
dy = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(Y)]

def bfs(x, y, d):
    count = 0
    que = deque()
    que.append((x, y, d))

    while que:
        x, y, d = que.popleft()

        if arr[x][y] == 0:
            arr[x][y] = 2  # 청소 완료 표시
            count += 1

        cleaned = False
        for i in range(4):
            nd = (d + 3 - i) % 4  # 왼쪽부터 반시계 방향 확인
            nx = x + dx[nd]
            ny = y + dy[nd]

            if 0 <= nx < Y and 0 <= ny < X and arr[nx][ny] == 0:
                que.append((nx, ny, nd))
                cleaned = True
                break

        if not cleaned:
            # 후진
            back = (d + 2) % 4
            bx = x + dx[back]
            by = y + dy[back]
            if 0 <= bx < Y and 0 <= by < X and arr[bx][by] != 1:
                que.append((bx, by, d))
            else:
                break

    return count

print(bfs(r, c, d))