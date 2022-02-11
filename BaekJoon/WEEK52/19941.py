'''
19941번 : 햄버거 분배
* 사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있음

-> 햄버거를 먹을 수 있는 사람의 최대 수

H P H P H P H H P P H P
K = 1
H P / H / P H / P H / H P / P H / P
H P / H P / H P / H / H P / P H / P

K = 2
H P / H P / H P / H H P P / H P

H H P H P P H H P P H P P P H P H P H P
H / H P / H P / P H / H P / P H / P P / P H / P H / P H / P

H H H H H P P P P P H P H P H P H H H P 
H H H / H H P P / P P / P H / P H / P H / P H / H / H P 

H H P P
H H H P P P
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bench = list(map(str, input()))

cnt = 0
for i in range(len(bench)):
    if bench[i] == "P":
        # 사람을 찾으면 왼쪽 햄버거부터 먹자
        for j in range(i-K, i+K+1):
            if 0 <= j < N and bench[j] == "H":
                cnt += 1
                bench[j] = 'E'
                break
                   
print(cnt)


# can = []
# for i in range(K):
#     ph = 'P'*(i+1)+'H'*(i+1)
#     hp = 'H'*(i+1)+'P'*(i+1)
#     can.append(hp)
#     can.append(ph)

# for i in range(len(can)):
#     bench = bench.replace(can[i], 'M')

# print(bench.count('M'))
