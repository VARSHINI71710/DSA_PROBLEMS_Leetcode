
#print odd numbers from 1 to 10 
for i in range (1,10,2):
                 print("The odd numbers are",i)


# loop in while
n = 123
sum = 0

while n > 0:
    sum = sum + (n % 10)   # add last digit
    n = n // 10            # remove last digit

print("The sum of the given integer:",sum)

