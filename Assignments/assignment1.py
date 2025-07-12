# Personal Health Monitoring System

user_id = int(input("Enter User ID: "))
user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your current weight in kg: "))
height = float(input("Enter your height in cm: "))
daily_steps = int(input("Enter the number of steps walked today: "))
health_conditions = list(input("Mention any known health conditions (separated by space): ").split())
vital_signs = tuple(map(float, input("Enter today's vital signs [Temperature(C), BP(High), BP(Low), Sugar level(mg/dL)]: ").split()))
medications = set(input("Enter medications you are currently taking (space-separated): ").split())
emergency_contact = eval(input("Enter your emergency contact details as a dictionary (e.g., {'Name':'Mom', 'Phone':9876543210}): "))

bmi = round(weight / ((height / 100) ** 2), 2)

user_info = {
    "Name": user_name,
    "ID": user_id
}

print()
print("Health Profile for", user_name)
print(f"Age: {age}, Weight: {weight}kg, Height: {height}cm")
print("BMI:", bmi)
print(f"Steps Walked Today: {daily_steps}")
print("Known Conditions:", ', '.join(health_conditions))
print("Vital Signs:")
print(f"  Temperature: {vital_signs[0]}°C")
print(f"  Blood Pressure: {vital_signs[1]}/{vital_signs[2]} mmHg")
print(f"  Sugar Level: {vital_signs[3]} mg/dL")
print("Medications:", ', '.join(medications))
print("Emergency Contact - Name: {Name}, Phone: {Phone}".format(**emergency_contact))
print("User: {Name}, ID: {ID}".format_map(user_info))

# Health Profile for Revanth  
# Age: 24, Weight: 75kg, Height: 178cm  
# BMI: 23.67  
# Steps Walked Today: 8000  
# Known Conditions: hypertension  
# Vital Signs:  
#   Temperature: 36.6°C  
#   Blood Pressure: 120/80 mmHg  
#   Sugar Level: 92 mg/dL  
# Medications: Amlodipine  
# Emergency Contact - Name: Mom, Phone: 9876543210  
# User: Revanth, ID: 1001
