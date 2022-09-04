def fibonacci_recursion(my_val):
   if my_val <= 1:
      return my_val
   else:
      return(fibonacci_recursion(my_val-1) + fibonacci_recursion(my_val-2))

while True:
    num_terms = int(input('Enter a number: '))
    if num_terms <= 0:
       print("Enter a positive integer...")
    else:
        print("The Fibonacci sequence is of", num_terms, 'is', end=' ')
        for i in range(num_terms):
            print(fibonacci_recursion(i), end=' ')
        break
