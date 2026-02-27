# Employee Attendance Tracker - Basic Version
import os
print("File saved at:", os.getcwd())
# Dictionary to store attendance data
attendance_data = {}

# Number of days to record
total_days = int(input("Enter total number of working days: "))

# Number of employees
num_employees = int(input("Enter number of employees: "))

for i in range(num_employees):
    name = input(f"\nEnter name of employee {i+1}: ")
    
    present_days = 0
    
    print(f"Enter attendance for {name}")
    print("Type P for Present, A for Absent")
    
    for day in range(total_days):
        status = input(f"Day {day+1}: ").upper()
        
        if status == "P":
            present_days += 1
    
    attendance_percentage = (present_days / total_days) * 100
    
    # Store in dictionary
    attendance_data[name] = {
        "Present Days": present_days,
        "Total Days": total_days,
        "Attendance %": attendance_percentage
    }

# ----------- REPORT -----------
print("\n📊 Attendance Report")
print("-" * 30)

for name, data in attendance_data.items():
    print(f"\nEmployee: {name}")
    print(f"Present Days: {data['Present Days']}")
    print(f"Total Days: {data['Total Days']}")
    print(f"Attendance Percentage: {data['Attendance %']:.2f}%")