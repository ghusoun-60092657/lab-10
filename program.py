import unittest
student_list = []
class TestStudentManagementSystem(unittest.TestCase):
    def test_Create_New_Student(self):
        #check if yes enter the new student fun
        print('Do you want to Enter a new student ? yes/no')
        new_student = input()
        # self.assertEqual(check(new_student), 'yes')
        if check(new_student) == 'no':return
        #check if the id is not null ,is integer,not negative,(id is not in the list)       
        id = input('Enter your id:')
        self.assertNotEqual(check(id),'','Ener a valid ID')
        self.assertEqual(check_int(id),True,'You should enter a numerical ID')
        self.assertGreater(check_negative(id),-1,'Enter a positive ID number')
        self.assertEqual(check_exist(id),False,'You should enter a new ID')

        #check if the age is not null ,is integer,not negative
        age = input('Enter your age:')
        self.assertNotEqual(check(age),'','Ener a valid Age')
        self.assertEqual(check_int(age),True,'You should enter a numerical Age')
        self.assertGreater(check_negative(age),0,'Enter an age of positive number')
        #check if the name is not null,is string
        name = input('Enter your name:')
        self.assertNotEqual(check(name),'','Ener a valid Name')
        self.assertEqual(check_int(name), False,'You should enter a string name')
        create_new_student(id,name,age)


def check(arg):
    return arg
def check_int(arg):
    return (arg.lstrip('-+').isdigit())
def check_negative(arg):
    return int(arg)
def check_exist(arg):
    if any(val['id'] == arg  for val in student_list):
        return True 
    else: return False


Test = TestStudentManagementSystem() 
# add a new student func
def create_new_student(id,name,age):
    student = {'id':id,'name':name, 'age':age}
    student_list.append(student)
    print('\nAdded to the list')
    Test.test_Create_New_Student()


# add retrieve student fun
def retrieve_student_info(id_):
    for i, val in enumerate(student_list):
       if val['id'] == id_:
           print('Your student information:')
           print('ID = ',val['id'],'\nname = ',val['name'],'  ','\nage = ',val['age'])

# add delete student fun
def delete_student(id_):
     for i, val in enumerate(student_list):
       if val['id'] == id_:
           student_list.pop(i)
           print('\nDeleted from the list')


if __name__ == '__main__':
    unittest.main()