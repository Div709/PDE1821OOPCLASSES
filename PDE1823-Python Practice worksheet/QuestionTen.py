# Question 10
class_info = {}
k = 0
total_marks = []
def get_grade(mark):
    if 80 <= mark <= 100:
        return "A"
    elif 70 <= mark <= 79:
        return "B"
    elif 60 <= mark <= 69:
        return "C"
    elif 50 <= mark <= 59:
        return "D"
    else:
        return "F"
student_no = int(input("Enter how many students in class: "))


while k < student_no:
    student_name = input(f"Enter student {k+1} name: ")
    student_grade = int(input(f"Enter {student_name} grade: "))
    class_info[student_name] = student_grade
    k += 1

for key, value in class_info.items():
    print(f"{key}- Mark: {value} - Grade: {get_grade(value)}")
    total_marks.append(value)
average_marks = sum(total_marks)/len(total_marks)
print(f"Class average: {average_marks:.2f}")
