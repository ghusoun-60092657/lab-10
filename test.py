import unittest
import program
#test if age < 20 bec its a student 
def check(arg):
    return arg
def check_int(arg):
    return isinstance(arg, int)
def check_negative(arg):
    if int(arg) > 0 :
        return True
    return False
def check_exist(arg,student_list):
    if any(obj['id'] == arg for obj in student_list):
        return True
    else:return False
class TestStudentManagementSystem(unittest.TestCase):
    def test_Create_New_Student_success(self):
        student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
        #check if the id is not null ,is integer,not negative,(id is not in the list)       
        id = 3
        #not empty
        self.assertNotEqual(check(id),'','Ener a valid ID')
        #number
        self.assertEqual(check_int(id),True,'You should enter a numerical ID')
        #positive
        self.assertEqual(check_negative(id),True,'Enter a positive ID number')
        #id is already exist 
        self.assertEqual(check_exist(id,student_list),False,'You should enter a new ID')

        #check if the age is not null ,is integer,not negative
        age = 21
        #not empty
        self.assertNotEqual(check(age),'','Ener a valid Age')
        #number
        self.assertEqual(check_int(age),True,'You should enter a numerical Age')
        #positive
        self.assertEqual(check_negative(age),True,'Enter an age of positive number')
        
        #check if the name is not null,is string
        name = 'ali'
        #not empty
        self.assertNotEqual(check(name),'','Ener a valid Name')
        #string
        self.assertEqual(check_int(name), False,'You should enter a string name')
        program.create_new_student(id,name,age,student_list)
    def test_Create_New_Student_fail(self):
        student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
        #check if the id is not null ,is integer,not negative,(id is not in the list)       
        id = -1
        #not empty
        self.assertNotEqual(check(id),'','Ener a valid ID')
        #number
        self.assertEqual(check_int(id),True,'You should enter a numerical ID')
        #positive
        self.assertEqual(check_negative(id),False,'Enter a positive ID number')
        #id is already exist 
        self.assertEqual(check_exist(id,student_list),False,'You should enter a new ID')

        #check if the age is not null ,is integer,not negative
        age = '21'
        #not empty
        self.assertNotEqual(check(age),'','Ener a valid Age')
        #number
        self.assertEqual(check_int(age),False,'You should enter a numerical Age')
        #positive
        self.assertEqual(check_negative(age),True,'Enter an age of positive number')
        
        #check if the name is not null,is string
        name = 2
        #not empty
        self.assertNotEqual(check(name),'','Ener a valid Name')
        #string
        self.assertEqual(check_int(name), True,'You should enter a string name')
        program.create_new_student(id,name,age,student_list)

class test_delete_student_details(unittest.TestCase):
        def test_To_Delete_By_ID_success(self):
            student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
            #check if the list is not empty ,id is not null,id is a number,id is in the list
            student_id = 1
            #not empty 
            self.assertNotEqual(check(student_id),'','Ener a valid student ID')
            #not number
            self.assertEqual(check_int(student_id),True,'You should enter a numerical ID')
            #not exist 
            self.assertEqual(check_exist(student_id,student_list),True,'You should enter an exist ID')
            program.delete_student(student_id,student_list)
        def test_To_Delete_By_ID_fail(self):
            student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
            #check if the list is not empty ,id is not null,id is a number,id is in the list
            student_id = 3
            #not empty 
            self.assertNotEqual(check(student_id),'','Ener a valid student ID')
            #not number
            self.assertEqual(check_int(student_id),True,'You should enter a numerical ID')
            #not exist 
            self.assertEqual(check_exist(student_id,student_list),False,'You should enter an exist ID')
            program.delete_student(student_id,student_list)
class test_get_student_details(unittest.TestCase):
        def test_To_Get_Data_By_ID_success(self):
            student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
            #check if the list is not empty ,id is not null,id is a number,id is in the list
            #list not empty **********
            # if len(student_list) == 0 :return
            student_id = 2
            #not empty
            self.assertNotEqual(check(student_id),'','Ener a valid student ID')
            #number
            self.assertEqual(check_int(student_id),True,'You should enter a numerical ID')
            #is exist in the list 
            self.assertEqual(check_exist(student_id,student_list),True,'You should enter an exist ID')
            program.retrieve_student_info(student_id,student_list)
        def test_To_Get_Data_By_ID_fail(self):
            student_list = [{'id':1,'name':'Dana','age':20},{'id':2,'name':'sara','age':18}]
            #check if the list is not empty ,id is not null,id is a number,id is in the list
            student_id = 4
            #not empty
            self.assertNotEqual(check(student_id),'','Ener a valid student ID')
            #number
            self.assertEqual(check_int(student_id),True,'You should enter a numerical ID')
            #is exist in the list should be false
            self.assertEqual(check_exist(student_id,student_list),False,'You should enter an exist ID')
            program.retrieve_student_info(student_id,student_list)
