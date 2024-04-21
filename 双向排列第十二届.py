
n, m = map(int, input().split())
list1 = []
list2 = list(range(1, n + 1))
for i in range(m):
    list1 = list(map(int, input().split()))
for a in list1:
    if list1[a] == 0:
        l2 = list2[:list1[a+1]]
        c=list2[list1[a+1]:]
        l2.sort()
        list2=l2+c
         
    elif list1[a] == 1:
        l2 = list2[1:list1[a]]
        c = list2[0]
        l2.sort(reverse=True)
        list2 = c + l2
    
for b in list2:
    print("{:d}".format(b), end=" ")

