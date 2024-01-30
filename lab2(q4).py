x = int(input("enter the first number in the range :"))
y = int(input("enter the second number in the range :"))
for i in range(x,y+1):
  if i>1:
    for num in range(2,i):
      if i%num==0:
        break
    else:
      print(i)
