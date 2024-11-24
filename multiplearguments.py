def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ", sum/len(numbers))



average(5,7,8,9,9,5,3,2)