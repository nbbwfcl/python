n = int(input())
for i in range(10000, 1000000):
    a = str(i)
    if a == a[::-1]:
        sum = 0  # 重新设置 sum 的值为 0
        for j in a:
            sum += int(j)  # 将字符串数字转换为整数并累加到 sum 中
        if sum == n:
            print(a)
            
