'''
14889번 : 스타트와 링크
* 사람 N명(짝수)
* N/2명으로 이루어진 스타트팀과 링크팀
* 사람에게 번호 1~N까지 부여
* S[i][j] : i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치 (S[i][j] != or == S[j][i])
* 팀의 능력치 = 팀에 속한 모든 쌍의 능력치의 합 

-> 팀의 능력치 차이를 최소로 하는 프로그램
'''

import sys
input = sys.stdin.readline
        
def dfs(depth, idx):
    global gap
    # 탈출조건
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        gap = min(gap, abs(start - link))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]
gap = int(1e9)

dfs(0, 0)
print(gap)