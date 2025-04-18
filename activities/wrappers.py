money = int(input("How much money do you have: "))

candy = money // 4
wrapper = candy

while wrapper >= 3:
    wrapper -=2
    candy += 1

total = candy
print(f"You can purchase {total} candy bars!")