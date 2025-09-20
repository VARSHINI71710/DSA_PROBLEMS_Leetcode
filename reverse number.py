n=int(input("A number: "))
count = 0
rev = 0
temp = n   

while temp != 0:
    digit=temp % 10    
    rev=rev * 10 + digit  
    temp=temp // 10       
    count=count+1             

print("No of digits =", count)
print("Reversed number =", rev)

#or

n=int(input())
str=str(n)
rev=int(str[::-1])