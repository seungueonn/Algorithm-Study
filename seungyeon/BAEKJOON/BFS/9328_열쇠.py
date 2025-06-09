from  collections import deque,Counter

def bfs():
    que=deque()
    que.append((0,0))

    visited=[[False for _ in range(X+2)] for _ in range(Y+2)]
    visited[0][0] = True

    cnt = 0

    while que:
        x,y=que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < X+2 and 0 <= ny <Y+2 and arr[ny][nx] != '*' and not visited[ny][nx]:
                
                if 'a' <= arr[ny][nx] <= 'z':
                    if not keys[arr[ny][nx]]:
                        keys[arr[ny][nx]] = True
                        visited=[[False for _ in range(X+2)] for _ in range(Y+2)]

                elif 'A' <= arr[ny][nx] <= 'Z':
                    if not keys[arr[ny][nx].lower()]:
                        continue

                elif arr[ny][nx] == '$':
                    cnt += 1
                    arr[ny][nx] = '.'

                visited[ny][nx] = True
                que.append((nx,ny))

    return cnt

t=int(input())

for _ in range(t):
    Y,X=map(int,input().split())

    arr=[['.'] * (X+2)]
    for _ in range(Y):
        arr.append(  ['.'] + list(input())  + ['.'] )
    arr.append(['.'] * (X+2))

    key_cnt=Counter(input())
    keys = {}

    for char in range(ord('a'), ord('z') + 1):
        if key_cnt[chr(char)] != 0:
            keys[chr(char)] = True
        else:
            keys[chr(char)] = False

    dx=[-1,1,0,0]
    dy=[0,0,1,-1]


    print(bfs())