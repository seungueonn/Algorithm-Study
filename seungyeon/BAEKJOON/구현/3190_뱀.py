# 뱀이 벽또는 자기 자신과 부딪히면 끝난다
# 뱀 시작 0,0 처음에 오른쪽을 향한다 
# 뱀의 이동. 사과가 있다면 꼬리 안 움직임, 없다면 꼬리 움직임(길이 유지)


import sys
from collections import deque

input=sys.stdin.readline

n=int(input().strip())
k=int(input().strip())
apple=[]
arr=[[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    y,x=map(int,input().split())
    apple.append((x,y))
    arr[y][x] = -1

l=int(input().strip())
dir={}
for _ in range(l):
    a,b=map(str,input().split())
    dir[int(a)] = b

dx=[1,0,-1,0] # 동남서북(시계방향) 오른쪽으로 90도 , 
dy=[0,1,0,-1]

# 뱀이 움직이다
def move(x,y,z):

    time = 0
    snake=deque()
    snake.append((x,y))
    time += 1
    arr[y][x] = time
    
    while True:

        # z 방향대로 나간다 
        nx = x + dx[z]
        ny = y + dy[z]

        if nx <= 0 or ny <= 0 or nx > n  or ny > n:
            print(time) # 벽에 부딪힘
            return 
        
        if arr[ny][nx] > 0: # 자기 자신을 만남
            print(time)
            return 

        if arr[ny][nx] == -1: # 사과 있음
            arr[ny][nx] = time
            snake.append((nx,ny))

        else: 
            rx,ry= snake.popleft()
            arr[ry][rx] = 0
            arr[ny][nx] = time
            snake.append((nx,ny))
            

        x,y=nx,ny

        if time in dir.keys():
            if dir[time] == 'D': # 오른쪽 회전
                z = (z+1) % 4 # 오른쪽 90도 회전
       
            else:
                z = (z-1) % 4

        time += 1

move(1,1,0)