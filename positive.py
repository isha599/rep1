list=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
ele=int(input())
list.append(ele)
print(list)
for num in list:
  if num>=0:
    print(num,end=" ")
