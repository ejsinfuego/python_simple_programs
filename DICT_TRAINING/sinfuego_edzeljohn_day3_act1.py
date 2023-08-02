name = str(input("Enter your name: "))
math = float(input("Enter your Math grade: "))
science = float(input("Enter your Science grade: "))
english = float(input("Enter your English grade: "))
grades = [math, science, english]

average = float((math + science + english)/3)

print("Average: ", average)
            
if average <= 75:
    print("Sorry you failed, the semester.")
elif average >= 75 and math > 75 and english > 75 and science > 75:
    print("Congratulations you passed the semester.")
elif average >= 75 and math < 75 or english < 75 or science < 75:
    if math < 75:
        if english < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take Math and English subject")
        elif science < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take Math and Science subject")
        else:
            print("Congratulations you passed the semester. But you need to re-enroll take Math subject")
    elif english < 75:
        if math < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take Math and English subject")
        elif science < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take English and Science subject")
        else:
            print("Congratulations you passed the semester. But you need to re-enroll take English subject")
    elif science < 75:
        if math < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take Math and Science subject")
        elif english < 75:
            print("Congratulations you passed the semester. But you need to re-enroll take English and Science subject")
        else:
            print("Congratulations you passed the semester. But you need to re-enroll take Science subject")
else:
    print("Congratulations you passed the semester.")



