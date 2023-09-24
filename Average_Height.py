# Input the heights as a string and split it into a list of heights
Student_Heights = input("Enter Heights: ").split()

# Convert the string heights to integers
for i in range(len(Student_Heights)):
    Student_Heights[i] = int(Student_Heights[i])

# Initialize variables to calculate the sum and average
total_height = 0
number_of_students = len(Student_Heights)

# Calculate the total height
for h in Student_Heights:
    total_height += h

# Calculate the average height
average_height = total_height / number_of_students

# Print the total and average height
print("Total height:", total_height)
print("Average height:", average_height)
