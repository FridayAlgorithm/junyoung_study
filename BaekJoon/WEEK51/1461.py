'''
1461번 : 도서관
* 현재 세준 위치 0, 책들의 위치 0
* 세준은 한번에 최대 M권 들 수 있음
* 한 걸음에 좌표 1칸

-> 각 책들을 원래 위치에 놔둘 때 드는 최소 걸음 수
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))  # 전체 책의 수, 한번에 들 수 있는 책의 수
book = list(map(int, input().split(' ')))
    
negative = []
positive = []
for b in book:
    if b < 0: 
        negative.append(abs(b))
    else : 
        positive.append(b)
    
steps = []
max_step = 0
negative.sort(reverse=True)
if negative:
    max_step = negative[0]
    i = 0
    while i < len(negative):
        steps.append(negative[i])
        i += M
        
positive.sort(reverse=True)
if positive:
    max_step = max(max_step, positive[0])
    i = 0
    while i < len(positive):
        steps.append(positive[i])
        i += M

answer = sum(steps)*2 - max_step
print(answer)


'''
음/양수를 분리

[-39, -37/ -29, -28/ -6 / 2, 11]
11 먼저 갔다옴
-6 하나만 갔다옴
-29 먼저 갔다옴
-39에서 멈춤

[-45, -26, -18/ -9, -4 /22, 40, 50]
-45 먼저 갔다옴
-9~0 갔다옴
50에서 멈춤

[-1 / 3 / 4, 5 / 6, 11]
[-12 / 3 / 4, 5 / 6, 11]

'''