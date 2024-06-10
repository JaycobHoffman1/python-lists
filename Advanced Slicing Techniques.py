# Task 1:
print('Task 1')

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temps_2nd_wk = temperatures[7:14]

print(f'The temperatures for the second week of the month are as follows: {temps_2nd_wk}')


# Task 2:
print('Task 2')

temps_above_100 = temperatures[temperatures.index(101):]

print(f'The temperatures above 100 are as follows: {temps_above_100}')


# Task 3:
print('Task 3')

temperatures.reverse()
temps_5th_to_10th = temperatures[4:10]

print(f"The temperatures from the fifth to the tenth day of the reversed list 'temperatures' are: {temps_5th_to_10th}")