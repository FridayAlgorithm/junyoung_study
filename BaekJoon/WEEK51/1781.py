'''
1782번 : 컵라면 
* N개의 문제
* 각 문제 당 받을 수 있는 컵라면 수
* 문제에는 데드라인이 있음 (N이하, 단위 시간 1)

-> 받을 수 있는 최대 컵라면 수
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
prob = []
for _ in range(N):
    d, c = map(int, input().split(' '))
    prob.append([d, c])
    
prob.sort()

queue = []
for deadline, cupnoodle in prob:
    heapq.heappush(queue, cupnoodle)
    if deadline < len(queue):
        heapq.heappop(queue)
        
print(sum(queue))