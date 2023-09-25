Student_Score = input("Input the scores: ").split()
for n in range(0,len(Student_Score)):
    Student_Score[n] = int(Student_Score[n])
print(Student_Score)

Highest_score = 0
for i in Student_Score:
    if i > Highest_score:
        Highest_score = i
print(f"The highest score is: {Highest_score}")