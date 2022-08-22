class FibFizzBizz:
    def __init__(self, f_num, l_num):
        self.f_num = f_num
        self.l_num = l_num

    # Function to convert integer to string
    def Formatt(num):
        assert type(num) == int, "Should be of integer type!"
        num = str(num)
        return num

    def PrintRange(f_num, l_num): 
        # Generate Fibonacci numbers.
        fib_numbers = [0,1]   
        r1 = fib_numbers[0]
        r2 = fib_numbers[1]
        
        for i in range(0, 101):
            rth = r1 + r2
            r1 = r2
            r2 = rth 
            fib_numbers.append(rth)
        
        # Loop to check the satisfaction of the set conditions.
        for i in range(f_num, l_num + 1):
            if i%3 == 0 and i%5 != 0 and i not in fib_numbers:
                print(FibFizzBizz.Formatt(i)+ "Fizz")

            elif i%3 != 0 and i%5 == 0 and i not in fib_numbers:
                print(FibFizzBizz.Formatt(i)+ "Buzz")

            elif i%3 == 0 and i%5 == 0:
                print(FibFizzBizz.Formatt(i) + "FizzBuzz")

            elif i in fib_numbers:
                print(FibFizzBizz.Formatt(i) + "Fibonacci")

            else:
                print(FibFizzBizz.Formatt(i) + " ")

           
FibFizzBizz.PrintRange(0,100)