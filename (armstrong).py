n = int(input("Enter a number: "))

num_str = str(n)
num_digits = len(num_str)

sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

if n == sum_of_powers:
    print(n, "is an Armstrong Number")
else:
    print(n, "is NOT an Armstrong Number")
