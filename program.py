
student_list = []
# add a new student func
def create_new_student():
    print('Enter your id:')
    id = input()
    print('Enter your name:')
    name = input()
    print('Enter your age:')
    age = input()
    student = {'id':id,'name':name, 'age':age}
    student_list.append(student)
    print('Do you want to Enter a new student ? yes/no')
    new_student = input()
    if new_student == 'yes':
        create_new_student()
print('Do you want to Enter a new student ? yes/no')
new_student = input()
if new_student == 'yes':
    create_new_student()