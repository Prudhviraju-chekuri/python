# Student Grade Tracker

student_id = input("Enter Student ID : ")
student_name = input("Enter Student Name : ")
attendance = input("Enter Attendance : ")
number_of_subjects = int(input("Enter No. of Subjects : "))
add_another_score_flag = "Yes"
sub_counter = number_of_subjects
total_score = 0
avg_score = 0



while sub_counter > 0 and (add_another_score_flag == "Yes" or add_another_score_flag == "yes"):
        
    score = int(input("Enter score :  " ))
    total_score = score + total_score
    sub_counter -= 1
    print(f"Total score : {total_score}")
    avg_score = total_score/number_of_subjects
    if sub_counter > 0:
        add_another_score_flag = input("Do you want to enter another score ? :")


print("******PERFORMANCE REPORT*****")
print("-----------------------------")
print(f"STUDENT ID : {student_id}")
print(f"STUDENT NAME : {student_name}")
print(f"ATTENDANCE : {attendance}")
print(f"NO. OF SUBJECTS : {number_of_subjects}")
print(f"TOTAL SCORE  : {total_score}")
print(f"AVERAGE SCORE : {round(avg_score,2)}")

if avg_score >= 85:
    print(f"PERFORMANCE : 'EXCELLENT'")
elif 70 <= avg_score <= 84:
    print(f"PERFORMANCE : 'GOOD'")
elif 50 <= avg_score <= 69:
    print(f"PERFORMANCE : 'AVERAGE'")
elif avg_score < 50:
    print(f"PERFORMANCE : 'NEEDS IMPROVEMENT'")

if int(attendance) < 75:
    print("WARNING : ATTENDANCE IS LOW")
