'''
1389번 : 케빈 베이컨의 6단계 법칙
* 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    steps = [0]*(N+1)
    visited = [start]
    
    queue = deque()
    queue.append(start)
    
    while queue:
        a = queue.popleft()
        for b in rel[a]:
            if b not in visited:
                steps[b] = steps[a]+1
                visited.append(b)
                queue.append(b)
            
    return sum(steps)

N, M = map(int, input().split(' ')) #유저 수, 친구관계 수
rel = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    rel[a].append(b)
    rel[b].append(a)
    
bacons = []
for i in range(1, N+1):
    bacons.append(bfs(i))
    
answer = bacons.index(min(bacons))+1
print(answer)