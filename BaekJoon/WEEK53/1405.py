'''
1405번 : 미친 로봇
* 로봇은 N번 행동
* 로봇은 4방향 중 하나를 선택하여 1칸 이동
* 같은 곳을 1번보다 많이 이동하지 않음 = 이동경로 단순

-> 로봇의 이동경로가 단순할 확률
'''

import sys
input = sys.stdin.readline

# 동, 서, 남, 북
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def dfs(y, x, p, visited):
    global answer
    if len(visited) == N+1:
        answer += p
        return
    
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if (ny, nx) not in visited:
            visited.append((ny, nx))
            dfs(ny, nx, p*percent[i], visited)
            visited.pop()
    
# N번, 동, 서, 남, 북 확률
N, east, west, south, north = map(int, input().split())
percent = [east/100, west/100, south/100, north/100]

answer = 0

dfs(0, 0, 1, [(0, 0)])
print(answer)