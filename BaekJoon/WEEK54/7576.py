'''
7576번 : 토마토
* 1 : 익은토마토 / 0 : 익지않은토마토 / -1 : 토마토X
* 익은 토마토 인접한 곳에 있는 익지 않은 토마토들은 영향을 받음
* 인접 : 상하좌우
* 저절로 익는 토마토는 없음
* 모두 익지 못한다면 -1

-> 토마토가 모두 익는 최소 일수 구하는 프로그램
'''

from collections import deque

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def ripen_tomato():
    queue = deque()
    # 익은 토마토들을 동시에 시작
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1: 
                queue.append((i, j))
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x]+1
                    queue.append((ny, nx))
        
ripen_tomato()                        
answer = 0
for b in box:
    if 0 in b:
        print(-1)
        exit(0)
    else:
        answer = max(answer, max(b))
print(answer-1)