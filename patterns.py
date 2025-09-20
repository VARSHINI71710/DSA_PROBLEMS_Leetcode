#patterns

n=5
for i in range (1,n+1):
    print("*" * i)
    


n=5
ch=65

for i in range(1,n+1):
    for j in range (i):
        print(chr(ch),end="")
        ch=ch+1
    print()