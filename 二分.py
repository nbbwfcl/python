from typing import List
def search(nums:List[int],target:int):
        left=0
        right=len(nums)-1
        while left<=right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            elif nums[middle]>target:
                right=middle-1
        return -1
a=search([1,2,3,4,5,7,9],5)

print(a)
