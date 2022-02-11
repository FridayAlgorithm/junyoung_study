''''
2529번 : 부등호
* '<', '>'가 k개 나열된 순서열 A
* 부등호 앞뒤에 숫자를 넣어서 부등호 관계 만족
* 부등호 관계를 만족하는 숫자는 여러 개

-> 해당 숫자들 중 최댓값과 최솟값 찾는 프로그램
'''

import sys
input = sys.stdin.readline

K = int(input())
sign = list(map(str, input().split()))

used = [False]*10 
max_num, min_num = "", ""

def check(a, b, s):
    if s == '<':
        if a < b: return True
        else: return False
    else:
        if a > b: return True
        else: return False

def find_num(idx, num):
    global max_num, min_num
    
    if idx == K+1:
        if min_num == "":
            min_num = num
        else:
            max_num = num
        return
    
    for i in range(10):
        if not used[i] and (idx == 0 or check(num[-1], str(i), sign[idx-1])):
            used[i] = True
            find_num(idx+1, num+str(i))
            used[i] = False
    
find_num(0, "")
print(max_num)
print(min_num)