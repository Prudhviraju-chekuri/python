class Student:
    student_name = "prudhvi"
    student_email = "ch.prudhvi@gmail.com"
    print(student_name,student_email)
    # method - defined inside the class
    #def info():
       # print(student_name)
        #print(student_email) # TypeError: Student.info() takes 0 positional arguments but 1 was given
    def info(self):
        print(self.student_name)
        print(self.student_email)
        #print(student_name)# NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        # without self student_name will be considered as local variables which are not defined hence the error
        # self lets method access object variables
        print(Student.student_name)# can be accessed with class name instead of self


# when we run this file, the statements inside a class will be executed automatically unlike function
# class call is not mandatory.
# functiona call is mandatory

# def a function
# call the function

#class object creation:
student_obj = Student()
print(student_obj)
print(student_obj.student_name)
print(student_obj.student_email)
student_obj.info()
# functions inside a class is a method

#Student.info()#TypeError: Student.info() missing 1 required positional argument: 'self'
# cannont be called with class name, only object name