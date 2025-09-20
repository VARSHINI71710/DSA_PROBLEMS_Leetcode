n=int(input("A number: "))
count = 0
rev = 0
temp = n   

while temp != 0:
    digit=temp % 10    
    rev=rev * 10 + digit  
    temp=temp // 10       
    count=count+1  

if(temp==rev):
    print("Palindrome")
else:
    print("Not a palindrome")


#or 

n=int(input())
str=str(n)
rev=int(str[::-1])
if (n==rev):
  print('Palindrome')
else:
  print('Not a palindrome')




#HCF/GCD

a=int(input())
b=int(input())

def gcd (a,b):
   while (b!=0):
      a,b=b,a%b
   return a


print("GCD (HCF) of", a, "and", b, "is:", gcd(a, b))
