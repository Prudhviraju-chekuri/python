# Create a comprehensive Python program and develop a simple console-based application that tracks student 
# grades for multiple subjects using loops, variables, data types, operators, type conversion, conditionals, 
# and input functions. This task demonstrates how loops solve real-world problems where the quantity of data 
# is unknown beforehand.
# 1. Collect Student Information:
# Student ID 
# Student Name 
# Attendance 
# Number of subjects
# Total Score 
# Continue input

# Collect student ID and validate using string methods
# While Reading ID, id should be positive 
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID:\n")
    # remove leading and trailing spaces.
    student_id = student_id.strip()
    # check if the given input is only numbers
    if student_id.isdigit() :
        student_id_valid = True
    elif student_id.startswith("-") and student_id.replace("-","").isdigit():
        print("Please Enter Positive Number or Above Zero")
    else:
        print("Please Enter Numbers Only. Other characters are not allowed")

# Collect student Name and validate using string methods
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter student name:\n")
        
    # remove leading and trailing spaces. Change to Title case
    student_name = student_name.strip().title()

    # name should be only alaphabets and also spaces allowed
    # name check with only spaces allowed
    student_name_check = student_name.replace(" ", "")

    # Minimum 3 characters length validation
    if student_name_check.isalpha() and len(student_name_check) > 3 :
        print("welcome " + student_name)
        student_name_valid = True
    elif not student_name_check.isalpha():
        print("Enter only alphabets. Other character are not allowed")
    else:
        print("Total characters should be greater than 3")

# Collect students attendance percentage and Validate
attendence_percentage_valid = False
while not attendence_percentage_valid :
    attendence_percentage = input("Enter student Attendance perctage:\n")
    # remove leading and trailing spaces.
    attendence_percentage = attendence_percentage.strip()
    # check if input is number and between 0 and 100
    if attendence_percentage.isdigit():
       attendence_percentage = int(attendence_percentage)
       if 0 <= attendence_percentage <=100 :
           attendence_percentage_valid = True
       else:
          print("Please Enter Number between 0 and 100")
    elif attendence_percentage.startswith("-") and attendence_percentage.replace("-","").isdigit():
        print("Please Enter Number between 0 and 100")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

# 2. Input Subject Scores:
# Repeatedly ask the user to enter scores for multiple subjects.
# Accepts "yes" or "Yes" as continuation options
# Add each entered score to the total score and increment the number of subjects.
# Continuation prompt: Ask the user if they want to enter another score after each entry 
# (allowing them to continue or stop inputting scores).

# Collect the score for subjects and validate
no_of_subjects = 0
total_score =0
while True:
    subject_score_valid = False
    while not subject_score_valid:
        subject_score = input(f"Enter the score of subject{no_of_subjects+1}:\n")
        # remove leading and trailing spaces.
        subject_score = subject_score.strip()
        if subject_score.isdigit():
            subject_score = int(subject_score)
            if subject_score <=100 :
                subject_score_valid = True
            else:
                print("Please Enter Number between 0 and 100")
        elif subject_score.startswith("-") and subject_score.replace("-", "").isdigit():
            print("Please Enter Number between 0 and 100") 
        else:
           print("Please Enter Numbers Only, Other characters not allowed") 
    total_score += subject_score
    no_of_subjects += 1
    # Continuation prompt validation
    continuation_prompt_valid = False
    while not continuation_prompt_valid:
        continuation_prompt = input("Do you want to enter score for more subjects? [Yes/No]:\n")
        continuation_prompt = continuation_prompt.strip()
        if continuation_prompt.lower() in ["yes", "no"] :
            continuation_prompt_valid = True
        else:
            print("Please enter only Yes or No")
    if continuation_prompt.lower() != "yes":
        break

# 3. Calculate Average Score:
# Calculate the average score for the student after all scores are entered.

average_score = total_score / no_of_subjects

# 4. Determine Performance Level:
# Use conditional statements to determine performance based on the average score:
# 85 and above → "Excellent"
# 70 to 84 → "Good"
# 50 to 69 → "Average"
# Below 50 → "Needs Improvement"

if average_score >= 85:
    performance_level = "Excellent"
elif average_score >= 70:
    performance_level = "Good"
elif average_score >= 50:
    performance_level = "Average"
else :
    performance_level = "Needs Improvement"

# 5. Check Attendance Status:
# Use a conditional statement to check if attendance is less than 75%. If so, 
# print a WARNING Low Attendance, else OK Attendance Satisfied

attendance_status = "WARNING Low Attendance" if attendence_percentage < 75 else "OK Attendance Satisfied"

# 6. Display Final Results:
# Print out the student’s ID, name, total score, 
# average score, performance level, and attendance 
# with appropriate messages.

print(f"\nStudent's ID : {student_id}")
print(f"Student's Name : {student_name}")
print(f"Total no of subjects : {no_of_subjects}")
print(f"Student's Totals scrore : {total_score}")
print(f"Student's Average scrore : {average_score:.1f}")
print(f"Student's Performance level : {performance_level}")
print(f"Student's Attendance : {attendence_percentage} % - {attendance_status}")