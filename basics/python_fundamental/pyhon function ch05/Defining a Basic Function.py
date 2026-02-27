# Given data
mark1 = 45
mark2 = 78
mark3 = 66

pass_marks = 50
marks_list = [45, 78, 66]

# 1. Arithmetic Operators
total = mark1 + mark2 + mark3
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)

# 2. Assignment Operator (add bonus marks)
total += 5
print("Total after adding bonus marks:", total)

# 3. Comparison Operator
is_pass_avg = average >= pass_marks
print("Passed based on average:", is_pass_avg)

# 4. Logical Operator
final_pass = (average >= pass_marks) and (mark3 >= pass_marks)
print("Final Pass Status:", final_pass)

# 5. Membership Operator
check_50 = 50 in marks_list
print("Is 50 in marks_list?", check_50)

# 6. Identity Operator
check_list = marks_list is not None
print("marks_list is not None:", check_list)

# 7. Bitwise Operator (Even / Odd check)
is_mark1_even = (mark1 & 1) == 0
print("Is mark1 even?", is_mark1_even)
