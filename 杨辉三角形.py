s=[[1]]#初始化列表s[0][0]=1
n=int(input())
for i in range(1,n):
    swap=s[-1]+[0]#创建一个名为 swap 的新列表。它将 s 中的最后一个子列表s[-1]
  #和包含一个元素 0 的列表进行连接。这样做的目的是为了为每一行的新列表添加一个0
    cul=[1]#确保每行第一个元素为1
    for j in range(len(swap)-1):
        cul.append(swap[j]+swap[j+1])
    s.append(cul)
for k in range(n):
    a=s[k]#遍历s的每一行
    for z in range(len(a)):#遍历每一行的每一个元素
        print(a[z],end=' ')
    print(' ')
    
