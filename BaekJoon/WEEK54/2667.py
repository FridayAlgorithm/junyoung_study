'''
2667번 : 단지번호 붙이기
* 1 : 집O, 0 : 집X
* 집의 모임(집이 상하좌우에 다른 집이 있는 경우) == 단지
* 단지에 번호를 붙임

-> 단지 수, 각 단지의 크기를 오름차순으로 정렬하여 출력
'''

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    ground[sy][sx] = 0
    count = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if ground[ny][nx] == 1:
                    count += 1
                    ground[ny][nx] = 0
                    queue.append((ny, nx))
                    
    return count

N = int(input())
ground = [list(map(int, input())) for _ in range(N)]
answer = []
                    
for i in range(N):
    for j in range(N):
        if ground[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()           
print(len(answer))
for ans in answer:
    print(ans)