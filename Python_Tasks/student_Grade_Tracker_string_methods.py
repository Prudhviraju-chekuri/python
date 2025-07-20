student_id = input("Enter the student ID\n")
if not student_id.isdigit():
    print("Student ID should be only numbers")
else:
    student_name = input("Enter student name\n")
    if not student_name.isalpha():
        print("Student name should be only alphabets")
    else:
        attendence_percent = input("Enter student Attendance perctage\n")
        if not attendence_percent.isdigit():
            print("Student's attendance percentage should be only numbers")
        elif 0 <= int(attendence_percent) >=100 :
            print("Student's attendance percentage should between 0 to 100")
        else:
            no_of_subjects = 0
            total_score =0
            while True:
                subject_score = int(input(f"Enter the score of subject{no_of_subjects+1}\n"))
                total_score += subject_score
                no_of_subjects += 1
                continuation_prompt = input("Do you want to enter score for more subjects? [Yes/No]\n")
                if continuation_prompt.lower() != "yes":
                    break
            average_score = total_score / no_of_subjects
            if average_score >= 85:
                performance_level = "Excellent"
            elif average_score >= 70:
                performance_level = "Good"
            elif average_score >= 50:
                performance_level = "Average"
            else :
                performance_level = "Needs Improvement"

            if int(attendence_percent) < 75:
                attendance_status = "WARNING Low Attendance"
            else :
                attendance_status = "OK Attendance Satisfied"
            print(f"\nStudent's ID : {student_id}")
            print(f"Student's Name : {student_name}")
            print(f"Total no of subjects : {no_of_subjects}")
            print(f"Student's Totals scrore : {total_score}")
            print(f"Student's Average scrore : {average_score:.1f}")
            print(f"Student's Performance level : {performance_level}")
            print(f"Student's Attendance : {attendence_percent} % - {attendance_status}")