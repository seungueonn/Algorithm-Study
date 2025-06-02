# import sys
# from collections import deque
# input=sys.stdin.readline

# Y,X,P=map(int,input().split())
# s = [0]+list(map(int,input().split()))

# cnt=[0] * (P+1)
# que=[deque() for _ in range(P+1)]


# arr=[[0] * X for _ in range(Y)]
# for i in range(Y):
#     a = list(map(str,input().strip()))
#     for j in range(X):
#         if a[j] == '.':
#             arr[i][j] = 0
#         elif a[j] == '#':
#             arr[i][j] = -1
#         else:
#             arr[i][j] = int(a[j])
#             que[int(a[j])].append((j,i))
#             cnt[int(a[j])] += 1


# # i번째 플레이어가 s[i] 만큼 성을 확장함 


# dx=[-1,1,0,0]
# dy=[0,0,1,-1]



# def bfs():

#     is_move=True

#     while is_move:
#         is_move = False

#         for i in range(1,P+1):

#             if not que[i]:
#                 continue
#             q = que[i]

#             for _ in range(s[i]): # z 만큼 움직임

#                 if not q:
#                     break
#                 for _ in range(len(q)):
#                     x,y=q.popleft()

#                     for j in range(4):
#                         nx = x + dx[j]
#                         ny= y + dy[j]

#                         if nx < 0 or ny < 0 or nx >= X or ny >= Y:
#                             continue
                        
#                         if arr[ny][nx] == 0:
#                             arr[ny][nx] = i
#                             q.append((nx,ny))
#                             is_move=True
#                             cnt[i] += 1

# bfs()
# print(*cnt[1:])

# # si 만큼 이동할 수 있는 모든 칸에 동시에 성을 만든다 

from collections import deque,defaultdict
import sys
input=sys.stdin.readline

Y,X,p=map(int,input().split())
players=[0] + list(map(int,input().split()))

arr=[]
players_que=defaultdict(deque)

answer=[0] * (p+1)


for i in range(Y):
    input_str=list(map(str,input().strip()))
    for j in range(X):
        if input_str[j] != '.' and input_str[j] != '#':
            players_que[int(input_str[j])].append((j,i))
            answer[int(input_str[j])] += 1
    arr.append(input_str)



# 동시에 이동
# 모든 플레이어가 확장할 수 없을 떄 끝남

extend_arr=[[0] * (X) for _ in range(Y)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs():

    is_move=True

    while is_move:
        is_move = False

        for i in range(1,p+1):

            if not players_que[i]:
                continue
            q = players_que[i]

            for _ in range(players[i]): # z 만큼 움직임

                if not q:
                    break
                for _ in range(len(q)):
                    x,y=q.popleft()

                    for j in range(4):
                        nx = x + dx[j]
                        ny= y + dy[j]

                        if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                            continue
                        
                        if arr[ny][nx] == '.':
                            arr[ny][nx] = i
                            q.append((nx,ny))
                            is_move=True
                            answer[i] += 1

bfs()
print(*answer[1:])