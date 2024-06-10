# Task 1:
print('Task 1')

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for grade in grades:
    if grade < 80:
        grade_index = grades.index(grade)

        print(f'Name: {students[grade_index]}')
        print(f'Grade: {grade}')
        print(f'Activity: {activities[grade_index]}')


# Task 2:
print("Task 2: This task adds students with grades 80 and above to the list 'students_approved'.")

students_approved = []
for grade in grades:
    if grade < 80:
        grade_index = grades.index(grade)
        '''
        (Not necessary for this task)
        print(f'Name: {students[grade_index]}')
        print(f'Grade: {grade}')
        print(f'Activity: {activities[grade_index]}')
        '''
    else:
        grade_index = grades.index(grade)

        students_approved.append(students[grade_index])


# Task 3:
print('Task 3')

print(f'The list of approved students is as follows: {students_approved}')