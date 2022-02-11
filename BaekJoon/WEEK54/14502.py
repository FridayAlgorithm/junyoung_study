'''
14502번 : 연구소
* 0 : 빈칸 / 1 : 벽 / 2 : 바이러스
* 바이러스는 상하좌우로 퍼질 수 있음
* 세울 수 있는 벽의 개수는 3개(무조건 세워야 함)
* 안전영역 == 바이러스가 퍼질 수 없는 곳

-> 안전 영역 크기의 최댓값을 구하는 프로그램
** pypy 제출
'''

from collections import deque
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

safezone = 0

def spread_virus():
    global safezone
    lab_ = copy.deepcopy(lab)
    
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab_[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if lab_[ny][nx] == 0:
                    lab_[ny][nx] = 2
                    queue.append((ny, nx))
    
    safezone = max(safezone, sum(l.count(0) for l in lab_))
    
    
def build_wall(wall):
    if wall == 3:
        spread_virus()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_wall(wall+1)
                lab[i][j] = 0

build_wall(0)  
print(safezone)