#Task 2: Calculate the average grade and print it.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
total = sum(grades)
average =total/len(grades)
print(grades)
print("The average grade is:", average)