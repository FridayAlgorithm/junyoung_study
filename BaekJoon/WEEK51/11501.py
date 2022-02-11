'''
11501번 : 주식
-> 날 별로 주식의 가격을 알려줄 때, 최대 이익
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split(' ')))
    
    # 피크 이전에 산 주식을 모두 판다.
    peak = 0 
    profit = 0
    for i in range(N-1, -1, -1):
        if stock[i] > peak:
            peak = stock[i]
            
        else:
            profit += peak-stock[i]
        
    print(profit)