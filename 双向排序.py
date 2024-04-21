n,m=map(int,input().split())
 
a=[list(map(int,input().split()))for i in range(m)]#二维数组，所以可以i[0]
 
b=list(range(1,n+1))
 
for i in a:
 
    if i[0]==0:
 
        c=b[:i[1]]
 
        d=b[i[1]:]
 
        c.sort(reverse=True)
 
        b=c+d
 
    else:
 
        c=b[:i[1]-1]#本题是从1开始算，2表示从第二位数开始升降排序，
        #而一个数列从0开始，所以要减一
 
        d=b[i[1]-1:]
 
        d.sort()
 
        b=c+d
 
print(*b)
