# 작성일자: 2024-04-20 SAT, 작성자: 이민영
# 백준 24313번 알고리즘 수업 - 점근적 표기 1

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if ((a1 * n0 + a0 <= c * n0)) and (a1 <= c):
    print(1)
else:
    print(0)
