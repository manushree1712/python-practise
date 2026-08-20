#  a dinner bill is 10,607 for 6 people.
#  calculate how much each person pays including an 18% tip.

number_of_people = 6


bill = 10607
bill_after_tip = (bill*18)/100
print(bill_after_tip)

bill_andtip = bill  + bill_after_tip
print(bill_andtip)


bill_for_each_person = bill_andtip/number_of_people
print(f"bill for rach person: {bill_for_each_person}")
