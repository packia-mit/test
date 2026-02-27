# 5-Year Child Health Tracker

# Step 1: Take inputs

sleep_hours = float(input("Enter number of hours child slept today: "))
play_minutes = int(input("Enter minutes of physical activity today: "))
water_glasses = int(input("Enter number of water glasses consumed: "))

# Step 2: Initialize health score
health_score = 0

# Step 3: Sleep Check
if sleep_hours >= 9:
    health_score += 1

# Step 4: Physical Activity Check
if play_minutes >= 60:
    health_score += 1

# Step 5: Water Intake Check
if water_glasses >= 5:
    health_score += 1

# Step 6: Final Health Status
print("\n----- Daily Health Report -----")

if health_score == 3:
    print("Health Status: EXCELLENT ⭐")
elif health_score == 2:
    print("Health Status: GOOD 👍")
else:
    print("Health Status: NEEDS IMPROVEMENT ⚠️")