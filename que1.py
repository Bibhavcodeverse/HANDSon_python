a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("A1 is gratest number")
elif(a2>a1 and a2>a3 and a3>a4):
    print("A2 is gratest number")
elif(a3>a1 and a3>a2 and a3>a4):
    print("A3 is gratest number")
else:
    print ("A4 is gratest number")
