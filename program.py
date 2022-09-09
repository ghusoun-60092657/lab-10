
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
# add retrieve student fun
def retrieve_student_info(id_):
    for i, val in enumerate(student_list):
       if val['id'] == id_:
           print ('name = ',val['name'],'  ','age = ',val['age'])
           break
       
print('Do you want to Retrieve student information? yes/no')
student_info = input()
if student_info == 'yes':
    print('Enter Student ID: ')
    student_id = input()
    retrieve_student_info(student_id)
# add delete student fun
def delete_student(id_):
     for i, val in enumerate(student_list):
       if val['id'] == id_:
           student_list.pop(i)
print('Do you want to Delete student information? yes/no')
student_delete = input()
if student_delete == 'yes':
    print('Enter Student ID to delete: ')
    student_id = input()
    delete_student(student_id)
print('Students list ',student_list)


