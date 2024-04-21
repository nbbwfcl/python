for i in range(100,1000):
    a=str(i)
    sum1=0
    res=[]
    for j in a:
        sum1+=int(j)**3#不能直接j**3+=i
    if sum1==i:#如果直接在内部循环结束时直接打印i，会导致在一次外部循环时可能
       # 会打印多次相同数字，应该在内部循环结束后直接打印数字
        print(i)
           
          
