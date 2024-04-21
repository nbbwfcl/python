n=int(input())
s=[]
count=1
for i in range(n+1):
    r=[]
    if i==0:
        r=[1]
    elif i==1:
        r=[1,1]
        count+=len(r)
    else:
        for j in range(i+1):
            if j==0 or j==i:
                r.append(1)
                count+=1

            else:
                a=s[i-1][j]+s[i-1][j-1]
                r.append(a)
                count+=1
                if a==n:
                    print(count)
                    exit()
    s.append(r)
if n==1:
    print(1)

                
                    
        

