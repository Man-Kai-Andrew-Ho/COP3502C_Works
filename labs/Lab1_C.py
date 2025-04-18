# This gets the year, month, and date for 1
year_1 = int(input("Enter the year for date 1: "))
month_1 = int(input("Enter the month for date 1: "))
date_1 = int(input("Enter the day for date 1: "))
# This gets the year, month, and date for 2
year_2 = int(input("Enter the year for date 2: "))
month_2 = int(input("Enter the month for date 2: "))
date_2 = int(input("Enter the day for date 2: "))
# This calculates the total dates
total_date_1 = (year_1 * 12 * 30) + (month_1 * 30) + date_1
total_date_2 = (year_2 * 12 * 30) + (month_2 * 30) + date_2
# This gets the difference between 1 and 2
diff = abs(total_date_2 - total_date_1)
# This prints the month/date/year for both 1 and 2 and the total days between the two dates
print(f"The difference between {month_1}/{date_1}/{year_1} and {month_2}/{date_2}/{year_2} is {diff} days!")