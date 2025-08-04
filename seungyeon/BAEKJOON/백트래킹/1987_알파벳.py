# import sys
# from collections import deque
# input = sys.stdin.readline
# r,c=map(int,input().split())

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# arr=[]
# visited=[]
# for i in range(r):
#     arr.append(list(input().strip()))
#     visited.append([False]*c)

# answer = set()
# ans = 0
# def back(x,y,cnt):
#     global ans

#     ans = max(ans,cnt)

#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]

#         if nx < 0 or ny < 0 or nx >= r or ny >= c:
#                 continue

#         if arr[nx][ny] not in answer :
#             answer.add(arr[nx][ny])
#             back(nx,ny,cnt+1)
#             answer.remove(arr[nx][ny])

# answer.add(arr[0][0])
# back(0,0,1)

# print(ans)


import sys
input=sys.stdin.readline

r,c=map(int,input().split())

arr=[]
for i in range(r):
    arr.append(list(map(str,input().strip())))

k=set()

dx=[-1,1,0,0]
dy=[0,0,1,-1]

answer=0

def dfs(x,y,cnt):

    global answer
    answer = max(answer,cnt)


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        if arr[nx][ny] not in k :
            k.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            k.remove(arr[nx][ny])


k.add((arr[0][0]))
dfs(0,0,1)


print(answer)