
x = int(input("Enter a value"))
y = int(input("Enter a value"))
z = int(input("Enter a value"))
n = int(input("Enter a value"))

def possible_coordinates():
    possible_values = [[i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0,z+1) if i+j+k != 1]
    print(possible_values)
    return possible_values

possible_coordinates()

