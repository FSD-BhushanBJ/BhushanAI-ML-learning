student_score = [150,52,63,45,85,96,145,185,201,42,552,639,1020,555,523,365]

# print(max(student_score))
max_num = 0

for high in student_score:
    if high > max_num:
        max_num = high
print(max_num)
