'''
2641번 : 다각형그리기
* 모양수열 : 1(오른쪽), 2(위쪽), 3(왼쪽), 4(아래쪽)
* 같은 다각형 여러 모양수열
* 다각형이 회전/뒤집어진 것은 같은 다각형X

-> 표본 모양수열과 같은 다각형을 그릴 수 있는 모양수열을 모두 찾는 프로그램
'''

import sys
input = sys.stdin.readline

L = int(input())  # 표본 모양수열의 길이
sample = list(map(str, input().split()))  # 원본 표본
sample_ = []  # 뒤집은 표본(순서, 방향)
for i in range(L-1, -1, -1):
    if sample[i] == '1': sample_.append('3')
    elif sample[i] == '2': sample_.append('4')
    elif sample[i] == '3': sample_.append('1')
    elif sample[i] == '4': sample_.append('2')

sam1 = ''.join(sample)
sam2 = ''.join(sample_)

E = int(input())  # 모양수열 개수
example = [''.join(input().split()) for _ in range(E)]
answer = []

def is_same(sample, ex):
    for i in range(L):
        tmp = ex[i:]+ex[0:i]
        if sample == tmp:
            return True
    return False

for i in range(E):
    if is_same(sam1, example[i]) or is_same(sam2, example[i]):
        answer.append(example[i])
        
print(len(answer))
for ans in answer:
    print(' '.join(ans))