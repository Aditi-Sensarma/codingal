work_day = int(input("Enter the total number of working days : "))
absent_day = int(input("Enter the total number of days absent : "))

present_day = work_day - absent_day
perc = (present_day/work_day)*100

print(f"Attendance percentage is : {perc}%")
if perc >= 75:
    print("You are allowed to sit for the exam")
else :
    print("You are not allowed to sit for the exam")