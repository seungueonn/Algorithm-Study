# # # import sys
# # # input=sys.stdin.readline

# # # arr=[]
# # # visited=[[0] * 5 for _ in range(5)]

# # # for i in range(5):
# # #     arr.append(list(map(str,input().strip())))

# # # # S 가 우위를 점해야함 적어도 7명중 4명 이상은 포함 되어있어야함
# # # dx=[-1,1,0,0]
# # # dy=[0,0,1,-1]


# # # def dfs(depth,answer,x,y):

# # #     visited[y][x] = 1

# # #     if depth == 7:
# # #         print(answer)
# # #         if answer.count('S') >= 4:
# # #             print(''.join(answer))
# # #             return 
        
# # #     for i in range(4):

# # #         nx = x + dx[i]
# # #         ny = y + dy[i]

# # #         if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
# # #             continue

# # #         if visited[ny][nx] == 0:

            
# # #             visited[ny][nx] = 1
# # #             answer.append(arr[ny][nx])
# # #             dfs(depth+1,answer,nx,ny)
# # #             answer.pop()
# # #             visited[ny][nx] = 0


# # # for i in range(5):
# # #     for j in range(5):
# # #         dfs(0,[],j,i)


# # # #  하지만 이 문제처럼 **“25명 중 7명을 골라서 연결 여부를 따지는 조합 문제”**에는 쓰면 안 됩니다.


# # import sys
# # from collections import deque
# # input=sys.stdin.readline

# # arr=[]
# # visited=[[0] * 5 for _ in range(5)]

# # for i in range(5):
# #     arr.append(list(map(str,input().strip())))

# # # S 가 우위를 점해야함 적어도 7명중 4명 이상은 포함 되어있어야함
# # dx=[-1,1,0,0]
# # dy=[0,0,1,-1]


# # def bfs(x,y):

# #     que=deque()

# #     bfs_visited=[[0] * 5 for _ in range(5)]

# #     que.append((x,y))

# #     bfs_visited[y][x] = 1
# #     cnt = 1

# #     while que:
# #         x,y=que.popleft()

# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]

# #             if 0 <= nx < 5 and 0 <= ny < 5 and bfs_visited[ny][nx] == 0 and visited[ny][nx] == 1: 
# #                 que.append((nx,ny))
# #                 bfs_visited[ny][nx] = 1
# #                 cnt += 1
# #     return cnt == 7 

# # def check(): # 현재시점 연결 여부 확인
# #     for i in range(5):
# #         for j in range(5):
# #             if visited[i][j] == 1:
# #                 return bfs(j,i)

# # def dfs(n, depth, s_cnt):

# #     global answer

# #     if depth > 7:
# #         return

# #     if n == 25:
# #         if depth == 7 and s_cnt >= 4:
# #             if check():
# #                 answer += 1 
# #         return 
    
# #     visited[n // 5][n % 5] = 1
# #     dfs(n+1,depth+1,s_cnt + int(arr[n//5][n% 5] == 'S'))
# #     visited[n // 5][n% 5] = 0
# #     dfs(n+1,depth,s_cnt)

# # answer = 0
# # dfs(0,0,0)
# # print(answer)

# from collections import deque
# import sys
# input=sys.stdin.readline

# arr=[]
# n=5
# for i in range(5):
#     arr.append(list(map(str,input().strip())))

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# # 주어진 값이 연결되어있는지 확인 (True/False)

# def bfs(nodes):  
#     que = deque()
#     visited = [False] * 25
#     node_set = set(nodes) # set 으로 만들어서 비교 대상 만들기

#     que.append(nodes[0])
#     visited[nodes[0][0] * 5 + nodes[0][1]] = True
#     count = 1

#     while que:
#         x, y = que.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < 5 and 0 <= ny < 5:
#                 if (nx, ny) in node_set and not visited[nx * 5 + ny]:
#                     visited[nx * 5 + ny] = True
#                     que.append((nx, ny))
#                     count += 1

#     return count == 7



# # 5*5 25 중에 7개 뽑기
# visited=[False]*n*n
# cnt = 0

# def back(start, path, s_count):
#     global cnt

#     # 종료 조건
#     if len(path) == 7:
#         if s_count >= 4 and bfs(path):
#             cnt += 1
#         return

#     for i in range(start, 25):  # 다음 인덱스부터만 탐색 → 중복 없는 조합
#         x, y = i//n,i%n
#         path.append((x, y))
#         back(i + 1, path, s_count + (arr[x][y] == 'S'))
#         path.pop()

# back(0, [], 0)
# print(cnt)




import sys
from collections import deque

input=sys.stdin.readline

n=5

arr=[]
for i in range(n):
    arr.append(list(map(str,input())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]

# S가 4명 이상이어야함

# 연결되어있는지 확인
def bfs(answer):
    que=deque()
    visited=[False]*n*n
    answer_set = set(answer)

    que.append(answer[0])
    visited[answer[0][0] * 5 + answer[0][1]] = True
    cnt = 1

    while que:
        x,y=que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx,ny) in answer_set and not visited[nx*5+ny]:
                    visited[nx*5+ny] = True
                    que.append((nx,ny))
                    cnt += 1

    return cnt == 7

# 자리 배치 조합

visited=[False]*n*n
cnt = 0

def back(start,answer,s_count):

    global cnt

    if len(answer) == 7:
        if s_count >=4 and bfs(answer):
            cnt += 1
        return 
    
    for i in range(start,25):
        x,y=i//n,i%n
        answer.append((x,y))
        back(i+1,answer,s_count + (arr[x][y] == 'S'))
        answer.pop()

back(0,[],0)
print(cnt)