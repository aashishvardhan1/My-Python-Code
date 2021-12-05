has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

if (has_good_credit or has_high_income) and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

# Logical AND = Both statements should be true
# Logical OR = Atleast One of the statements is true
#Logical NOT is to invert the boolean Value