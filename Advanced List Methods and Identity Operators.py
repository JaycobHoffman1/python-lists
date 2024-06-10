# Task 1:
print('Task 1')

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for name in submitted:
    if name in submitted and name in attended:
        print(f'{name} both submitted their assignment and attended the class.')


# Task 2:
print('Task 2')

print("The lists 'submitted' and 'attended' are identical!" if submitted is attended \
else "The lists 'submitted' and 'attended' are not identical.")


# Task 3:
print('Task 3')

for name in attended:
    if name not in submitted:
        attended.remove(name)
        
print(f"The 'attended' list without those who did not submit their assignment is as follows: {attended}")