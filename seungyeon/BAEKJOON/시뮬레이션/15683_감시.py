# import sys
# import copy
# input=sys.stdin.readline
# n,m=map(int,input().split())

# cctv=[]
# arr=[]

# mode = [
#     [],
#     [[0],[1],[2],[3]],
#     [[0,2],[1,3]],
#     [[0,1],[1,2],[2,3],[0,3]],
#     [[0,1,2],[1,2,3],[0,2,3],[0,1,3]],
#     [[0,1,2,3],]
# ]

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]


# for i in range(n):
#     data=list(map(int,input().split()))
#     arr.append(data)
#     for j in range(m):
#         if data[j] in [1,2,3,4,5]:
#             cctv.append([data[j],i,j])

# def fill(board,mode,x,y):
#     for i in mode:
#         nx=x
#         ny=y

#         while True:
#             nx += dx[i]
#             ny += dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 break

#             if board[nx][ny] == 6:
#                 break

#             elif board[nx][ny] == 0:
#                 board[nx][ny] = -1


# def dfs(depth,board):
#     global min_value

#     if depth == len(cctv):
#         count = 0

#         for i in range(n):
#             count += board[i].count(0)

#         min_value=min(min_value,count)
#         return 
    
#     tmp = copy.deepcopy(board)
#     cctv_num,x,y = cctv[depth]
#     for i in mode[cctv_num]:
#         fill(tmp,i,x,y)
#         dfs(depth+1,tmp)
#         tmp = copy.deepcopy(board)

# min_value = int(1e9)
# dfs(0,arr)
# print(min_value)


# # import sys
# # import copy

# # input=sys.stdin.readline
# # Y,X=map(int,input().split())

# # arr=[]
# # cctv=[]
# # for i in range(Y):
# #     input_arr = list(map(int,input().split()))
# #     arr.append(input_arr)
# #     for j in range(X):
# #         if input_arr[j] in [1,2,3,4,5]:
# #             cctv.append([input_arr[j],j,i]) # x,y


# # dir=[
# #     [],
# #     [[0],[1],[2],[3]],
# #     [[0,2],[1,3]],
# #     [[1,2],[1,3],[3,0],[0,1]],
# #     [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
# #     [[0,1,2,3],]

# # ]

# # dx=[-1,1,0,0]
# # dy=[0,0,1,-1]

# # def check(arr,dir,x,y):

# #     for i in dir:
# #         nx=x
# #         ny=y

# #         while True:
# #             nx += dx[i]
# #             ny += dy[i]

# #             if nx < 0 or ny < 0 or nx >= X or ny >= Y:
# #                 break

# #             if arr[ny][nx] == 6:
# #                 break

# #             elif arr[ny][nx] == 0:
# #                 arr[ny][nx] = -1

# # def dfs(arr,depth):
# #     global min_value

 
# #     if depth == len(cctv): # cctv 개수만큼
# #         count = 0

# #         for i in range(Y):
# #             count += arr[i].count(0)

# #         min_value=min(min_value,count)
# #         return 
    
# #     tmp = copy.deepcopy(arr)
# #     cctv_num,x,y=cctv[depth]

# #     for i in dir[cctv_num]:
# #         check(tmp,i,x,y)
# #         dfs(tmp,depth+1)
# #         tmp = copy.deepcopy(arr)

# # min_value=int(1e9)
# # dfs(arr,0)
# # print(min_value)



import sys
import copy

Y,X=map(int,input().split())

input_arr=[]
cctv=[]
for i in range(Y):
    input_i=list(map(int,input().split()))
    input_arr.append(input_i)
    for j in range(X):
        if input_i[j] in [1,2,3,4,5]:
            cctv.append([input_i[j],j,i])


cctv_dir=[

    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3],]
]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def fill(arr,dir,x,y):

    for i in dir:
        nx = x
        ny = y

        while True:

            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                break

            if arr[ny][nx] == 6:
                break

            if arr[ny][nx] == 0:
                arr[ny][nx] = -1

    

def dfs(depth,arr):

    global min_value


    if depth == len(cctv):
        cnt = 0

        for i in range(Y):
            cnt += arr[i].count(0)

        min_value=min(min_value,cnt)

        return
        
    cctv_mode,x,y=cctv[depth]

    tmp = copy.deepcopy(arr)

    for i in cctv_dir[cctv_mode]:
        fill(tmp,i,x,y)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)

min_value=int(1e9)
dfs(0,input_arr)
print(min_value)