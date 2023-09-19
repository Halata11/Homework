students = int(input())
count2to3 = 0
count3to4 = 0
count4to5 = 0
count5to6 = 0
sumGrades = 0
for i in range(students):
    grade = float(input())
    if grade<2 or grade>6:
        print("Wrong grade")
        exit()
    if grade < 3:
        count2to3 += 1
    elif grade < 4:
        count3to4 += 1
    elif grade < 5:
        count4to5 += 1
    else:
        count5to6 += 1
    sumGrades += grade
percent2to3 = count2to3 / students * 100
percent3to4 = count3to4 / students * 100
percent4to5 = count4to5 / students * 100
percent5to6 = count5to6 / students * 100
avgGrade = sumGrades / students
print(f"Top students: {percent5to6:.2f}%")
print(f"Between 4.00 and 4.99: {percent4to5:.2f}%")
print(f"Between 3.00 and 3.99: {percent3to4:.2f}%")
print(f"Fail: {percent2to3:.2f}%")
print(f"Average: {avgGrade:.2f}")
