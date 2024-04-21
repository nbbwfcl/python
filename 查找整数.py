n=int(input())
num=list(map(int,input().split()))#num=map(int(input().split(' ')))
a=int(input())

if a in num:
         print(num.index(a)+1)
else:
    print(-1)
         
