'''
3079번 : 입국심사
* 총 M명, N개의 입국심사대
* k번 심사대에 앉아있는 심사관이 1명을 심사하는데 드는 시간 Tk
* 1개의 심사대에서는 1번에 1명만 심사
* 가장 앞에 서 있는 사람은 빈 심사대로 이동할 수 있음
 
-> 심사를 받는데 걸리는 시간의 최솟값
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))  #입국심사대 수, 사람 수
time = [int(input()) for _ in range(N)]

answer = 0
start, end = 0, M*max(time)
while start <= end:
    checked = 0
    mid = (start + end)//2
    
    for t in time:
        checked += mid // t
        
    if checked >= M:
        answer = mid
        end = mid-1
    else:
        start = mid+1
        
print(answer)