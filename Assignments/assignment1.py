# Student Profile System

student_id = int(input("Enter Student ID: "))
student_name = input("Enter your name: ")
gpa = float(input("Enter your current GPA (out of 10): "))
subjects = list(input("Enter your enrolled subjects: ").split())
marks = tuple(map(int, input("Enter marks for each subject: ").split()))
extracurriculars = set(input("Enter your extracurricular activities: ").split())
contact_details = eval(input("Enter your contact details as a dictionary (e.g., {'Phone':1234567890,'Email':'abc@example.com'}): "))
scholarship_percentage = float(input("Scholarship percentage awarded: "))

student_info = {
    "Name": student_name,
    "ID": student_id
}

print()
print("Student_name, ID: ", end="")
print(student_name, student_id, sep=",")
print(f"GPA: {gpa}")
print("Scholarship: %.2f%%" % scholarship_percentage)
print("Contact Info - Phone: {Phone}, Email: {Email}".format(**contact_details))
print("Name: {Name}, ID: {ID}".format_map(student_info))


# Student_name, ID: Revanth,945
# GPA: 9.16
# Scholarship: 75.00%
# Contact Info - Phone: 9347296933, Email: revanthbalabhadruni@gmail.com
# Name: Revanth, ID: 945