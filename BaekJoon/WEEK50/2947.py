'''
2947번 : 나무 조각
* 나무 조각 5개를 가지고 있고, 1~5번 숫자
* 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만듦
'''
import sys
input = sys.stdin.readline

piece = list(map(int, input().split(' ')))
num = 5

while True:
    switch = 0
    for i in range(num-1):
        if piece[i] > piece[i+1]:
            tmp = piece[i+1]
            piece[i+1] = piece[i]
            piece[i] = tmp

            switch += 1
            print(' '.join(map(str, piece)))
    
    if switch == 0:
        break