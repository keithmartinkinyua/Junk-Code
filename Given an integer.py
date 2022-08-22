n = int(input("Enter an interger"))

def given_an_interger(n):
    if n % 2 == 1:
        print("Wierd")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not wierd")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Wierd")
    elif n > 20:
        print("Wierd")


given_an_interger(n)
