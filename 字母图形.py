row,cul=list(map(int,input().split()))
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list1=list(str)
for i in range(row):
    if i==0:
        print(str[:cul])
    else:
        str=list1[i]+str#从B开始循环，每循环一次读取一个数，拼接str
        print(str[:cul])


              


              
