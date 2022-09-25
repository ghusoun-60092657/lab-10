# add a new student func
def create_new_student(id,name,age,student_list):
    student = {'id':id,'name':name, 'age':age}
    student_list.append(student)
    # print(student_list)
    print('\nAdded to the list')


# add retrieve student fun
def retrieve_student_info(id_,student_list):
    for i, val in enumerate(student_list):
       if val['id'] == id_:
           print('Your student information:')
           print('ID = ',val['id'],'\nname = ',val['name'],'  ','\nage = ',val['age'])

# add delete student fun
def delete_student(id_,student_list):
     for i, val in enumerate(student_list):
       if val['id'] == id_:
           student_list.pop(i)
           print('\nDeleted from the list')



