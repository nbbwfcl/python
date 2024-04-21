def coin_change(coins, amount):
    coins.sort(reverse=True)  # 按照面额从大到小排序
    num_coins = 0
    for coin in coins:
        num_coins += amount // coin  # 使用尽可能多的当前面额的硬币
        amount %= coin
    if amount == 0:
        return num_coins
    else:
        return -1  # 无法凑出总金额

# 示例用法
coins = [1, 2, 5, 10, 20, 50, 100]
amount = 123
print("最少硬币数量:", coin_change(coins, amount))
