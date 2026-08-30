math = int(input("enter math marks out of 100: "))
phy = int(input("enter phy marks out of 100: "))
chem = int(input("enter chem marks out of 100: "))

total_marks = math + phy + chem

print(f"total marks: {total_marks}")

average_marks = (total_marks / 300) * 100

print(f"average marks: {average_marks}")

if total_marks >= 250:
    print("your grade is A+")

elif 200 <= total_marks < 250:
    print("your grade is A")

elif 175 <= total_marks < 200:
    print("your grade is B")

elif 100 <= total_marks < 175:
    print("your grade is C")

else:
    print("your grade is D")