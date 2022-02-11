'''
2110번 : 공유기 설치
* 집의 개수는 N개
* 같은 좌표를 갖는 집은 없음
* 공유기를 C개 설치하려고 할 때, 최대한 많은 곳에서 와이파이 사용할 수 있도록
* 한 집에는 공유기 1개 설치하고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게

-> 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
   (최소가 최대가 되로록)
'''

import sys
input = sys.stdin.readline

def router_count(dist):
    cnt = 1
    now = home[0]
    for i in range(1, N):
        if home[i] >= now+dist:
            cnt += 1
            now = home[i]
    return cnt
            
N, C = map(int, input().split(' ')) # 집 수, 공유기 수
home = [int(input()) for _ in range(N)]
home.sort()

answer = 0
start, end = 1, home[-1]-home[0]
while start <= end:
    router = 0
    mid = (start+end)//2
    
    if router_count(mid) >= C:
        answer = mid
        start = mid+1
    else:
        end = mid-1
        
print(answer)