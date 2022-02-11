'''
1520번 : 내리막길
* 직사각형 지도, 각 칸에는 그 지점의 높이
* 지도에서 상하좌우 이웃한 곳끼리만 이동 가능
* 목표지점 : 제일 오른쪽 아래칸
* 항상 높이가 더 낮은 지점으로만 이동
'''

import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]
    
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]
print(dfs(0, 0))