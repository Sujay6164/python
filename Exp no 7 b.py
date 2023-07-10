def create_student_details():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    if age < 0:
        raise NegativeAgeException(age)  
    marks = []
    for i in range(1, 6):
        subject_mark = int(input(f"Enter mark for subject {i}: "))
        marks.append(subject_mark)
        student_details = {"name": name,"age": age,"marks": marks}
    return student_details
try:
   student = create_student_details()
   print("Student Details:")
   print(student)
except NegativeAgeException :
    print("invalid age")
