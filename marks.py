import pdb;pdb.set_trace()

def calculate_grade_marks(score):
    breakpoint()

    marks = int(input("Enter marks:"))
    if marks>= 70:
        grade='A'
    elif marks >=60:
        grade='B'
    elif marks>=50:
        grade='C'
    elif marks>=40:
        grade='D'
    else:
        grade='F'
    print(grade)
score= float(input("enter the student's score:"))
grade = calculate_grade_marks(score)
print(f'the student grade is: {grade}')
