x=int(input("enter an integer number :"))
y=1
fact=1
if x<0:
  print("ther is no factorial for negative number : try again ")
elif x==0:
  print("factorial is :"+str(1))
else :
  while y<=x:
    fact*=y
    y+=1
  print("factorial of the number is :"+str(fact))
# another solution by using range function 
'''x=int(input("enter a number : "))
fact=1
if x<0:
  print("ther is no factorial for negative number : try again ")
elif x==0:
  print("factorial is :"+str(1))
else :
   for i in range(1,x+1):
    fact*=i
   print("factorial is :"+str(fact))
'''