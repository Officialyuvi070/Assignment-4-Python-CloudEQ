# Recursive Function
# A function which calls itself which used to directly
# use a mathematically formula as a function it can loop
# itself to reach an answer. it can slip into function which
# never terminates.

# WAP using recursive function.

# Program to print the fibonacci series upto n_terms

# Recursive function
def fibonacci(n):
    if n <= 1:
	    return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n_terms = 20

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
	print(fibonacci(i))