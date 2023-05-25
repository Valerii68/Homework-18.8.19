N = int(input("How many tickets do you need? "))
bill = 0
age = [int(input("How old is each visitor? ")) for i in range(1, N + 1)]
for a in age:
    if a > 100 or a <= 0:
        raise ValueError("Wrong age")
else:
    for a in age:
        if a < 18:
            bill = bill
        elif 18 <= a <= 25:
            bill += 990
        else:
            bill += 1390
    if N > 3:
        total_bill = bill - bill * 10 / 100
        print(f"Your price: {bill} rubles \nDiscount: {bill*10 / 100} rubles \nYour final price: {total_bill} rubles")
    else:
        total_bill = bill
        print(f"Your price: {total_bill} rubles")
