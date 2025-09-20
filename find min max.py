#min and max array

arr = eval(input("Enter an integer array: "))

# find maximum and minimum
maximum = max(arr)
minimum = min(arr)

print("Maximum element in the array:", maximum)
print("Minimum element in the array:", minimum)


#Write a Python program to check whether a given string is a palindrome or not.

s=input("Enter a string: ")
if s==s[::-1]:              #string[start : stop : step](move forward or backward)
    print("Its is a palindrome")
else :
    print("It is not a palindrome")