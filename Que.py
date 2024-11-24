English= int (input("Marks obtaoined in English: "))
Science= int (input("marks obtained in Science: "))
Sanskrit= int (input("marks obtained in Sanskrit: "))
Social_Science = int (input("marks obtained in Social Science: "))
Maths =  int (input("marks obtained in Maths : "))
total_marks=500
Total_marks_obtained = (English+Science+Sanskrit+Social_Science+Maths)
Percentage = (Total_marks_obtained/total_marks)*100

print(Percentage)

if(Percentage>=40 and English>33 and Science>33 and Sanskrit>33 and Social_Science>33 and Maths>33):
    print("You are pass")
else:
    print("You failed, try again next year! ")

