n = int(input("Please enter a positive integer: "))
def factor(n):
    result = 1
    for i in range(1, n+1):
        result *=i
    return result
result = factor(n)
if n < 0:
    print("Invalid Number")
elif n == 0:
    print("Invalid Number")
else:
    print("The factorial of", n, "is:", result)
        
        
    
