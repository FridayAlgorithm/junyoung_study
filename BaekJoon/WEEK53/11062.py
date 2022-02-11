'''
11062번 : 카드 게임
* N개의 카드에는 점수가 있음
* 한 턴에는 가장 왼쪽에 있는 카드나 가장 오른쪽의 카드 가져갈 수 있음 (근우부터)
* 카드가 더이상 남아있지 않을 때까지 반복
* 점수 = 카드의 점수의 합

-> 근우가 얻은 점수
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    
'''
그리디 문제X -> DP 문제
dp[i][j] : i~j의 카드가 있을 때 선택할 수 있는 최대 값

'''