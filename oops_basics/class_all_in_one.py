class Student:
    def __init__(self,student_name,student_email):
        self.student_name= student_name
        self.student_email= student_email

    def info(self):
        print("Student name:",self.student_name)
        print("Student email:",self.student_email)

student_one = Student("one", "one@gmail.com")
student_two = Student("two", "two@gmail.com")

student_one.info()
student_two.info()