def fibonacci(num):
    fib_numbers = [0,1]   
    n1 = fib_numbers[0]
    n2 = fib_numbers[1]
    for i in range(0, num):
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        fib_numbers.append(nth)
        print(fib_numbers)
    return fib_numbers
    
fibonacci(50)




