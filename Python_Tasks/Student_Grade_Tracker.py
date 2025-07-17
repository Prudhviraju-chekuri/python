
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

student_id = input("Enter the student ID\n")
student_name = input("Enter student name\n")
attendence_percent = int(input("Enter student Attendance perctage\n"))

# 2. Input Subject Scores:
# Repeatedly ask the user to enter scores for multiple subjects.
# Accepts "yes" or "Yes" as continuation options
# Add each entered score to the total score and increment the number of subjects.
# Continuation prompt: Ask the user if they want to enter another score after each entry 
# (allowing them to continue or stop inputting scores).

no_of_subjects = 0
total_score =0
while True:
    subject_score = int(input(f"Enter the score of subject{no_of_subjects+1}\n"))   
    total_score += subject_score
    no_of_subjects += 1
    continuation_prompt = input("Do you want to enter score for more subjects? [Yes/No]\n")
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

if attendence_percent < 75:
    attendance_status = "WARNING Low Attendance"
else :
    attendance_status = "OK Attendance Satisfied"

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
print(f"Student's Attendance : {attendence_percent} % - {attendance_status}")