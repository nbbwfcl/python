Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> n=int(input())
a=[]
a.append(input())
for i in a:
	if 1<=len(a)<=200:
		b=a.sorted()
		for i in range(0,n):
			print(b[i],end=' ')