'''
2812번 : 크게 만들기
* N자리 숫자가 주어졌을 때, 숫자 K개를 지워서 얻을 수 있는 가장 큰 수
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
num = list(input().strip())

result = []
cnt = K
for i in range(N):
    while cnt > 0 and result:
        if result[-1] < num[i]:
            result.pop()
            cnt -= 1
        else:
            break
    
    result.append(num[i])
        
print(''.join(result[:N-K]))