from datetime import datetime

filename = f"attendance_{datetime.now().strftime('%Y%m%d')}.csv"

import csv
from datetime import datetime

attendance_data = {}

total_days = int(input("Enter total number of working days: "))
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
    
    attendance_data[name] = {
        "Present Days": present_days,
        "Total Days": total_days,
        "Attendance %": attendance_percentage
    }

# ----------- SAVE TO CSV -----------
filename = "attendance_report.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Header row
    writer.writerow(["Employee Name", "Present Days", "Total Days", "Attendance %"])
    
    for name, data in attendance_data.items():
        writer.writerow([
            name,
            data["Present Days"],
            data["Total Days"],
            f"{data['Attendance %']:.2f}"
        ])

print(f"\n✅ Attendance saved to {filename}")

# ----------- SIMPLE SUMMARY REPORT -----------
print("\n📊 Summary Report")
print("-" * 40)

for name, data in attendance_data.items():
    status = "GOOD" if data["Attendance %"] >= 75 else "LOW"
    
    print(f"{name} → {data['Attendance %']:.2f}% ({status})")