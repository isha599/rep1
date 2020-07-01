num=int(input("total terms :"))
n1,n2=0,1
c=0
if num<=0:
  print("enter a positive integer")
elif num==1:
  print("fibonacci sequence upto:",num)
  print(n1)
else:
  print("fibonacci sequence:")
  while c<num:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    c=c+1
