# import sys
# from collections import deque,defaultdict

# n,m=map(int,input().split())

# visited=[[False] * (n+1) for _ in range(n+1)]
# lights=[[False] * (n+1) for _ in range(n+1)]

# light=defaultdict(list)

# for i in range(m):
#     x,y,a,b=map(int,input().split())
#     light[(x,y)].append((a,b))


# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# # 1,1에서 시작해서 가장 많은 방의 불을 켜는 방법

# def bfs(x,y):
#     answer = 1

#     que=deque()
#     que.append((x,y))

#     visited[x][y] = True
#     lights[x][y] = True

#     while que:
#         x,y=que.popleft()

#         for a,b in light[(x,y)]:
#             if not lights[a][b]:
#                 lights[a][b] = True
#                 answer += 1

#                 for i in range(4):
#                     nx = a + dx[i]
#                     ny = b + dy[i]

#                     if nx <= 0 or ny <= 0 or nx > n or ny > n:
#                         continue

#                     if visited[nx][ny]:
#                         que.append((nx,ny)) # 방문한 적 있으면 새로 연결되어 또 불 켤 곳이 있을 수 있음
                        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx <= 0 or ny <= 0 or nx > n or ny > n:
#                 continue

#             if not visited[nx][ny] and lights[nx][ny]: # 첫방문인데 불 켜진 곳 
#                 que.append((nx,ny))
#                 visited[nx][ny] = True

#     return answer
    
# cnt = 0
#  # 1,1에서 시작하지만 스위치가 없는 경우? 는 없음 -> 그냥 1
# print(bfs(1,1))

from collections import deque,defaultdict


import sys
input=sys.stdin.readline

n,m=map(int,input().split())

light=defaultdict(list)

for i in range(m):
    x,y,a,b=map(int,input().split())

    light[(x,y)].append((a,b))

visited=[[0] * (n+1) for _ in range(n+1)]
lights=[[False] * (n+1) for _ in range(n+1)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    
    que=deque()
    que.append((x,y))
    answer=1

    visited[x][y] = True
    lights[x][y] = True

    while que:
        x,y=que.popleft()

        for a,b in light[(x,y)]:
            if not lights[a][b]:
                lights[a][b] = True
                answer += 1

                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]

                    if nx < 0 or ny < 0 or nx > n or ny > n:
                        continue

                    if visited[nx][ny]:
                        que.append((nx,ny))


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n or ny > n:
                continue

            if not visited[nx][ny] and lights[nx][ny]:
                que.append((nx,ny))
                visited[nx][ny] = True

    return answer

print(bfs(1,1))