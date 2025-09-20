watt = int(input("Enter the watt: "))

if watt >= 1 and watt <= 100:
    print(f"The total amount is ₹ {watt * 5}")
elif watt >= 101 and watt <= 200:
    print(f"The total amount is ₹ {watt * 7}")
else:
    print(f"The total amount is ₹ {watt * 9}")
