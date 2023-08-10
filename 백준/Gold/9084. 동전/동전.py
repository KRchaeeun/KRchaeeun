import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input()) # 동전의 가지 수
    coins = list(map(int, input().split()))
    M = int(input()) # 만들어야 할 금액
    dp = [0] * (M + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i - coin]


    print(dp[M])
