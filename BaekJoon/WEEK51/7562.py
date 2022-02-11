'''
7562번 : 나이트의 이동
* 나이트가 한번에 이동할 수 있는 칸

-> 몇 번 움직이면 원하는 칸으로 이동할 수 있는가?
'''

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def cnt_moving(start, goal):
    queue = deque()
    queue.append(start)
    
    sx, sy = start
    gx, gy = goal
    board[sx][sy] = 1
    while queue :
        x, y = queue.popleft()
        if x == gx and y == gy:
            return board[x][y]-1
        for i in range(8):
            nx , ny = x+dx[i], y+dy[i]
            if 0 <= nx < le and 0 <= ny < le and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1
    
T = int(input())
for _ in range(T):
    le = int(input())
    board = [[0]*le for _ in range(le)]
    
    start = list(map(int, input().split(' ')))
    goal = list(map(int, input().split(' ')))
    
    answer = cnt_moving(start, goal)
    print(answer)