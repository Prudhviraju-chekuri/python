# Use Tuples for storing system information(immutable)
# use dictionaries for storing the complex student information
# use LISTS for storing multiple scores
# use SETS for storing multiple scores
# From web application point of view [CRUD operation]
# C- create, R- Read, U- Update , D- Delete

# Implement student management system(part of LMS)

# System information to be stored(tuples)
SYSTEM_INFO = ("LMS Students Portal","v1.0","2025","EDIFY University")
ADMIN_INFO = ("admin@edify.ai","+91-9989555487","201")
#Display system info
print("="*50)
print(f"Welcome to {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
print(f"Developed by {SYSTEM_INFO[3]} in the year {SYSTEM_INFO[2]}")
print("="*50)

# Implement functionalities
# stores students information
students = {}

# design menu systems for operation
while True:
    print("Enter choose an option:")
    print("1- Add student")
    print("2- Modify student")
    print("3- Delete student")
    print("4- List student")
    print("5- Exit Application")

    choice = input("Enter your Choice(1-5)")
    if choice == "1":
       print("Performing choice 1 operation")
       student_id = input("Enter student ID")
       if student_id in students:
           print("student already exists")
       else:
           name = input("Enter student name").strip().title()
           #store multiple scores
           scores = []
           while True:
               score_input = input("Enter a score or type Done")
               if score_input == "Done":
                   break
               if score_input.isdigit():
                   score = int(score_input)
                   if 0 <= score <= 100:
                       scores.append(score)
                   else:
                       print("Invalid score, only 0-100")
               else:
                   print("Invalid score, only numbers accepted")

           # store multiple skills
           skills = set()
           while True:
               skill_input = input("Enter a skill or type Done")
               if skill_input == "Done":
                   break
               skills.add(skill_input.strip().title())

           # save student detailsb
           students[student_id] = {
               "name": name,
               "scores": scores,
               "Skills": skills
           }
           print(f"students data{students}")
               
    elif choice == "2":
        print("Performing choice 2 operation")
        student_id = input("Enter the student ID")
        if student_id in students:
            new_name = input("Enter new name")
            students[student_id]["name"] = new_name
            print(f"students data{students}")
        else:
            print("Student doesn't exixts")
    elif choice == "3":
        print("Performing choice 3 operation")
        student_id = input("Enter the student ID to delete")
        removed = students.pop(student_id)
        if removed:
            print("Student removed succesfully")
        else:
            print("Student doesn't exists")
    elif choice == "4":
        print("Performing choice 4 operation")
    elif choice == "5":
        print("Performing choice 5 operation")
        break
    else:
        print("Invalid Entry. Choose 1-5")
