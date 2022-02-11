'''
1197번 : 최소 스패팅 트리

그래프가 주어졌을 때, 그 그래프의 최소 스패팅 트리
-> 그래프의 모든 정점을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

A, B 정점이 가중치 C 간선으로 이루어짐
'''

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
root = [i for i in range(V+1)]
edge = []
for _ in range(E):
    edge.append(list(map(int, input().split())))
    
edge.sort(key=lambda x: x[2])  # 가중치로 정렬

def find_root(n):
    if n != root[n]:
        root[n] = find_root(root[n])
    return root[n]

answer = 0
for a, b, c in edge:
    a_root = find_root(a)
    b_root = find_root(b)
    
    # 두 정점의 root가 다르다면 하나의 루트로 연결
    if a_root != b_root:
        if a_root > b_root:
            root[a_root] = b_root
        else:
            root[b_root] = a_root
        answer += c
    print(root)
        
print(answer)