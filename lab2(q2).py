x = int(input("enter the length of the rectangular :"))
y = int(input("enter the width of the rectangular :"))

for i in range (1,x+1):
  for w in range (1,y+1):
    if i==1 or i==x or w==1 or w==y:
      print("*",end="")
    else:
      print(" ",end="")
  print()