'''
11052번 : 카드 구매하기
* 카드에는 8등급의 컬러
* 카드는 카드팩 형태로만 구입 가능 -> 1~N개가 포함된 카드팩(N가지)
* 카드 i개가 포함된 카드팩은 Pi원
* 민규는 돈을 최대한 많이 지불해서 카드 N개 구매
'''

import sys
input = sys.stdin.readline

N = int(input())
p = [0] + list(map(int, input().split(' ')))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+p[j])

print(dp[-1])


'''
dp[2] = dp[1] + p[1] or dp[0] + p[2]
dp[3] = dp[2] + p[1] or dp[1] + p[2] or dp[0] + p[3]
dp[4] = dp[3] + p[1] or dp[2] + p[2] or dp[1] + p[3] or dp[0] + p[4]
'''