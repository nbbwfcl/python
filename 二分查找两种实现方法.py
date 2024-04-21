#二分查找条件：有序的数列、数据量不能太大也不能太小
#纯算法方式
'''arr_list=[5,7,11,22,27,33,29,52,58]
number=13#要查找的数字
count=0
left=0#序列左侧的索引
right=len(arr_list)-1#序列右侧的索引
while left<=right:
    middle=(left+right)//2
    count+=1
    if number>arr_list[middle]:
        left=middle+1

    elif number<arr_list[middle]:
        right=middle-1

    else:
        print(f'数字{number}已找到，索引值为{middle}')
        break
else:
    print(f'数字{number}没有找到')
print(f'一共用了{count}次查找')'''

#递归方法
arr_list=[5,7,11,22,27,33,29,52,58]
def binary_search(number,left,right):
    if left<=right:
        middle=(left+right)//2
        if number<arr_list[middle]:
            right=middle-1
        elif number>arr_list[middle]:
            left=middle+1
        else:
            return middle
        return binary_search(number,left,right)
    else:
        return -1
print(binary_search(11,0,len(arr_list)-1))
    
    

