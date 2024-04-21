from typing import List
height=[4,3,2,1,4]
 def maxArea(self, height: List[int]) -> int:
        Area=[]
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                c=j-i
                h=min(height[i],height[j])
                area=c*h
                Area.append(area)
        return max(Area)
#超出时间限制
#双指针，和二分法有类似
def maxArea(self, height: List[int]) -> int:
        i,j,area=0,len(height)-1,0#二分模板类似
        while i<j:#二分模板类似
            if height[i]<height[j]:
                area=max(area,(j-i)*height[i])
                i+=1
            else:
                area=max(area,height[j]*(j-i))
                j-=1
        return area 
            
