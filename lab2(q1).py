x = 1
ma=mi=int(input("enter the the numbers :"))  # here is the first number entered by user
su=ma=mi
while x < 10:
    y = int(input())
    if y > ma:
        ma = y
    elif y < mi:
        mi = y
    su+=y
    x += 1
print("max value is :" + str(ma))
print("min value is :" + str(mi))
avg=su/10
print("average value is :"+str(avg))
# another way to solve this problem
'''
x = 0
m = set()
print("enter ten values please: ")
while x < 10:
    y = int(input())
    m.add(y)
    x += 1
print("the maximum value is : " + str(max(m)))
print("the minimum value is : " + str(min(m)))
print("the average value is : " + str(sum(m) / 10))
'''