n=int(input())
a=[]
for i in range(n):
    b=int(input(),16)#输入的直接用list存储
    c=str(oct(b))
    d=int(c[2:])
    a.append(d)
for i in range(n):
    print(a[i])
