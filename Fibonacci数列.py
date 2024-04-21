n=int(input())

def f(n):
    if n==1 or n==2:
        return 1
    else:
     return f(n-1)%10007+f(n-2)%10007
print(f(n))

