list1=[]
n=int(input())
for i in range(n+1):
    list2=[]
    if n==0:
        list2=[1]
    elif n==1:
        list2=[1,1]
    else:
        for j in range(i+1):
            if j==0 or j==i:
                list2.append(1)#最后appendlist1
            else:
                list2.append(list1[i-1][j]+list1[i-1][j-1])
    list1.append(list2)
print(list1)
