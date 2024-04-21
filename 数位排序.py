n=int(input())
m=int(input())
list2=[]
list3=[]
for i in range(1,n+1):
     list3.append(i)
     list1=[int(a) for a in str(i)]
     b=sum(list1)
     list2.append(b)
di=dict(zip(list3,list2))#将两个列表转成字典
res=sorted(di.items(),key=lambda x:x[1],reverse=False)#按值的大小排序
dire={}
for i in res:
    dire[i[0]]=i[1]#将元组 i 的第一个元素作为键，第二个元素作为值
list3=list(dire.keys())
#print(dire)
print(list3[m-1])
            
        
    
