'''
1911번 : 흙길 보수하기
* 폭우가 내려서 N(1<=N<=10,000)개의 물웅덩이 생김
* 물웅덩이를 덮을 수 있는 길이 L짜리 널빤지를 충분히 갖고 있음
* 물웅덩이의 위치와 크기가 주어짐

-> 모든 물웅덩이를 덮기 위해 필요한 널빤지의 최소 개수
'''
import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split(' ')) # 물웅덩이 수, 널빤지 길이
puddle = []
for _ in range(N):
    puddle.append(list(map(int, input().split(' '))))
puddle.sort(key=lambda x: x[0])

now, plank = 0, 0 # 현재 위치, 널빤지 수
for i in range(N):
    if now < puddle[i][0]: # 현재 위치가 현재 물웅덩이보다 이전이면
        now = puddle[i][0] # 현재 물웅덩이 시작으로 이동
        
    p_cnt = math.ceil((puddle[i][1]-now)/L) # 올림
    now += (p_cnt*L) # 널빤지 끝으로 이동
    plank += p_cnt 

print(plank)

# . . . M M M M . M M M M . . .
# . . . _ _ _ _ _ _ _ _ _
