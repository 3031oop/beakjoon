X = int(input()) # 총 금액
N = int(input()) # 물건의 종류의 수
cal_X = 0

for i in range(N):
    a, b = map(int,input().split())
    cal_X += a * b

if X == cal_X:
    print("Yes")
else:
    print("No")