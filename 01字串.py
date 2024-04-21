for i in range(32):
    a=str(bin(i))
    b=a[2:]
    #print(b)
    #print("{:0>5d}".format(b))
    print("{:0>5}".format(b))#字符串无需加d，如果格式化的是整数值则需加上d

