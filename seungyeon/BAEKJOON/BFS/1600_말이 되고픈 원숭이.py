# # k번만 이동 가능. 그외에는 인접한 칸으로 이동

# import sys
# from collections import deque
# input=sys.stdin.readline


# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# hdx=[-1,-2,1,2,-1,-2,1,2]
# hdy=[2,1,2,1,-1,-2,-2,-1]

# # hdx=[1,2]
# # hdy=[2,1]
# k=int(input())

# w,h=map(int,input().split())
# arr=[]

# for i in range(h):
#     arr.append(list(map(int,input().split())))

# visited=[[0] * w for _ in range(h)]

# def bfs(x,y,k):

#     que=deque()
#     que.append((x,y))

#     while que:

#         x,y=que.popleft()

#         if k >= 0:
#             for j in range(8):

#                 hx = x + hdx[j]
#                 hy = y + hdy[j]
                
#                 if hx < 0 or hy < 0 or hx >= w or hy >= h:
#                     continue
                
#                 if visited[hy][hx] == 0 and arr[hy][hx] == 0:
#                     visited[hy][hx] = visited[y][x] + 1
#                     que.append((hx,hy))
#                     k -= 1
            
#         else:
#             for i in range(4):
#                 nx=x + dx[i]
#                 ny=y + dy[i]
                
                
#                 if nx < 0 or ny < 0 or nx >= w or ny >= h:
#                     continue

#                 if visited[ny][nx] == 0 and arr[ny][nx] == 0:
#                     visited[ny][nx] = visited[y][x] + 1
#                     que.append((nx,ny))
#     return -1


# bfs(0,0,k)

# if visited[h-1][w-1] == 0: print(-1)
# else: print(visited[h-1][w-1])



# k번만 이동 가능. 그외에는 인접한 칸으로 이동

import sys
from collections import deque
input=sys.stdin.readline


dx=[-1,1,0,0]
dy=[0,0,1,-1]

hdx=[-1,-2,1,2,-1,-2,1,2]
hdy=[2,1,2,1,-1,-2,-2,-1]

# hdx=[1,2]
# hdy=[2,1]
k=int(input())

w,h=map(int,input().split())
arr=[]

for i in range(h):
    arr.append(list(map(int,input().split())))

visited=[[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

def bfs(x,y,z,k):

    que=deque()
    que.append((x,y,z))
    visited[y][x][z] = 0

    while que:

        x,y,z=que.popleft()

        if y == h-1 and x == w-1:
            return visited[y][x][z]


        if z < k:
            for j in range(8):

                hx = x + hdx[j]
                hy = y + hdy[j]
                
                if hx < 0 or hy < 0 or hx >= w or hy >= h:
                    continue
                
                if visited[hy][hx][z+1] == -1 and arr[hy][hx] == 0:
                    visited[hy][hx][z+1] = visited[y][x][z] + 1
                    que.append((hx,hy,z+1))
                    
            
        for i in range(4):
            nx=x + dx[i]
            ny=y + dy[i]
        
                
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if visited[ny][nx][z] == -1 and arr[ny][nx] == 0:
                visited[ny][nx][z] = visited[y][x][z] + 1
                que.append((nx,ny,z))
    return -1


print(bfs(0,0,0,k))




