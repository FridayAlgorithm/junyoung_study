'''
14226번 : 이모티콘
* 스마일 이모티콘 S개 보냄
* 이미 화면에 1개 입력
* 남은 이모티콘 입력
    1. 화면의 이모티콘 모두 복사해서 클립보드에 저장 (덮어쓰기)
    2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣음
    3. 화면에 있는 이모티콘 중 하나 삭제
* 각 연산은 1초 걸림

-> S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값
'''

import sys
from collections import deque
input = sys.stdin.readline

S = int(input())

queue = deque()
queue.append((1, 0)) # 화면, 클립보드

visited = dict()
visited[(1, 0)] = 0

while queue:
    sc, cb = queue.popleft()
    if sc == S:
        print(visited[(sc, cb)])
        break
    
    # 1. 화면의 이모티콘 모두 복사해서 클립보드에 저장
    if (sc, sc) not in visited.keys():
        visited[(sc, sc)] = visited[(sc, cb)] + 1
        queue.append((sc, sc))
    
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣음
    if (sc+cb, cb) not in visited.keys():
        visited[(sc+cb, cb)] = visited[(sc, cb)] + 1
        queue.append((sc+cb, cb))
        
    # 3. 화면에 있는 이모티콘 중 하나 삭제
    if (sc-1, cb) not in visited.keys():
        visited[(sc-1, cb)] = visited[(sc, cb)] + 1
        queue.append((sc-1, cb))