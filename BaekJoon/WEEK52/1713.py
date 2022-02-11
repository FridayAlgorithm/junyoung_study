
import sys
input = sys.stdin.readline

N = int(input())
total = int(input())
reco = list(map(int, input().split()))

'''
1. 추천학생이 후보인지 확인
2. 이미 후보라면, 추천수 증가
3. 더 이상 자리가 없다면, 추천수 낮은 순서&먼저 들어온 순서로 삭제
[학생번호, idx, recommend]
'''
def is_candidate(i):
    for c in range(len(cand)):
        if cand[c][0] == reco[i]:
            return c
    return -1
    
cand = [[reco[0], 0, 1]]
for i in range(1, total):
    
    # 이미 후보라면
    idx = is_candidate(i)
    if idx != -1:
        cand[idx][2] += 1 # 추천 수 상승
    else:
        cand.sort(key=lambda x: (x[2], x[1]))
        # 자리가 있고, 
        if len(cand) < N:
            cand.append([reco[i], i, 1]) # 후보등록
        # 자리가 없고,
        else:
            cand[0] = [reco[i], i, 1] # 후보교체
    
cand.sort(key=lambda x: x[0])
final = []
for i in range(len(cand)):
    final.append(cand[i][0])
    
print(*final)