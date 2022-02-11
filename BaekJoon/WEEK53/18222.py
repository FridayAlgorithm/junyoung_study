'''
18222번 : 투에-모스 문자열
* 0과 1로 이루어진 무한한 문자열 X

-> X의 k번째에 오는 문자
'''

import sys
input = sys.stdin.readline

k = int(input())

def thue_morse(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return thue_morse(n//2)
    else:
        return 1-thue_morse(n//2)
    
print(thue_morse(k-1))