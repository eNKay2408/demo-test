n, k = map(int, input().split())

time_left = 240 - k
time_solve = 5
res = 0

for i in range(n):
    if time_left >= time_solve:
        time_left -= time_solve
        time_solve += 5
        res += 1
    else:
        break

print(res)
