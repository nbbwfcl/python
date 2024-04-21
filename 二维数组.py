a=int(input('请输入两个数字：')
rray1=[]
rownum=[]
#循环遍历空格分割字符串
for i in a.split(' '):
      rray1.append(int(x))
#重新命名行和列
row=rray1[0]
cul=rray1[1]
#双层遍历出行和列
for i in range(row):
      culnum=[]
      for j in range(cul):
          culnum.append(j)
      #print(culnum)
      rownum.append(culnum)
print(rownum)

            
