# Task 1:
print('Task 1')

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()

print(f"The list 'grades' sorted in descending order is as follows: {grades}")


# Task 2:
print('Task 2')

sum_of_grades = 0
for grade in grades:
    sum_of_grades += grade

average = sum_of_grades // len(grades)

print(f'The average grade is {average}.')


# Task 3:
print('Task 3')

for grade in grades:
    if grade < 80:
        grades[grades.index(grade)] = 'Failed'
        
print(f"The list 'grades' with all values below 80 replaced with 'Failed' is as follows: {grades}")