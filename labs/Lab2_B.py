total_income = float(input("Enter your total income this year: "))
owed_taxes = 0
if total_income > 609351:
    owed_taxes = ((total_income - 609350) * 0.37) + ((609350 - 243725) * 0.35) + ((243725 - 191950) * 0.32) + ((191950 - 100525) * 0.24) + ((100525 - 47150) * 0.22) + ((47150 - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 243726:
    owed_taxes = ((total_income - 243725) * 0.35) + ((243725 - 191950) * 0.32) + ((191950 - 100525) * 0.24) + ((100525 - 47150) * 0.22) + ((47150 - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 191951:
    owed_taxes = ((total_income - 191950) * 0.32) + ((191950 - 100525) * 0.24) + ((100525 - 47150) * 0.22) + ((47150 - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 100526:
    owed_taxes = ((total_income - 100525) * 0.24) + ((100525 - 47150) * 0.22) + ((47150 - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 47151:
    owed_taxes = ((total_income - 47150) * 0.22) + ((47150 - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 11601:
    owed_taxes = ((total_income - 11600) * 0.12) + ((11600 - 0) * 0.10)
elif total_income > 0:
    owed_taxes = total_income * 0.10

print(f"You owe ${owed_taxes:.2f} this year.")