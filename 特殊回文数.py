n=int(input())

list1=[]
#if n>1 and n<54:
for i in range(10000,1000000):
    a=str(i)
    if a==a[::-1]:
        list1.append(a)
for j in list1:
    k=list(map(int,j))#map(function,list1[])，接收一个函数和一个列表，把函数依次
    #作用在列表的每一个元素上，并且返回一个新列表,map函数需要进过list转换
         
    if sum(k)==n:
        print(j)
            
          
