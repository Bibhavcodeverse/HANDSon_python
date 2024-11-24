import time 

t=time.strftime('%H:%M:%S')


hour =int(time.strftime("%H"))

mintues= int(time.strftime("%M"))

second= int(time.strftime("%S"))

hour=int(input("Enter hour: "))
mintues=int(input("Enter mintues: "))
second=int(input("Enter second: "))


print(hour)
print(mintues)
print(second)





if (hour>=0 and hour<12):
    print("Good Morning Sir!")

elif (hour>=12 and hour<17):
    print("Good Afternoon Sir!")

elif (hour>=17 and hour<0):
    print("Good night Sir!")


