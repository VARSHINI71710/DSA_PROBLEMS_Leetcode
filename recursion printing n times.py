def fun(n):
    if n > 0:
        print("Hello Varshini")
        fun(n-1)

fun(5)

def print_name(name, n):
    if n > 0:                  
        print(name)            
        print_name(name, n - 1)


print_name("Varshini", 5)


def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)  
        print(n)             

print_numbers(5)



def print_reverse(n):
    if n > 0:              
        print(n)           
        print_reverse(n-1) 

print_reverse(5)