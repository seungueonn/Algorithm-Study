# import sys
# from collections import deque
# input=sys.stdin.readline

# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# 한 점에서 다른 점으로 가는데 최단거리
# 점의 끝을 알아야함
# 유니온파운드와 bfs의 차이 


# 최단거리 구하기 
# def find(x,y):
#     global answer

#     que = deque()
#     cnt = 1

#     que.append((x,y))
#     while que:

#         x,y=que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue

#             if arr[ny][nx] == 1 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 print(nx,ny)
#                 answer=min(answer,cnt)
#                 print(answer)
#                 return 

#             if arr[ny][nx] == 0 and not visited[ny][nx]:
#                 cnt += 1
#                 que.append((nx,ny))

# # 배열의 끝자리를 찾아서 
# def bfs(x,y):


#     que = deque()

#     que.append((x,y))
#     while que:

#         x,y=que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue

#             if arr[ny][nx] == 1 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 que.append((nx,ny))

#             if arr[ny][nx] == 0 and not visited[ny][nx]:
#                 find(x,y)

# answer=int(1e9)

# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             bfs(i,j)

# print(answer)

from collections import deque
import sys
input = sys.stdin.readline
 
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
 
# 섬의 개수를 구하고 섬마다 번호를 표시하는 bfs
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    maps[x][y] = mark
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
 
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = mark
                    visited[nx][ny] = True
 
# 섬 사이 최단거리를 구하는 bfs
def bfs2(island):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            if maps[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != island and maps[nx][ny] != 0: # 다른 섬과 만났을 경우
                    return dist[x][y]
                if maps[nx][ny] == 0 and dist[nx][ny] == -1: # 물이고 아직 건너지 않은 곳일 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
 
mark = 1 # 섬마다 번호를 체크하기 위한 값
for x in range(n):
    for y in range(n):
        if maps[x][y] == 1 and not visited[x][y]:
            island_cnt = bfs(x, y)
            mark += 1
 
result = sys.maxsize # 최솟값을 구하기 위해 가장 큰 값으로 세팅
for island in range(1, mark):
    result = min(result, bfs2(island))
 
print(result)