# Set data
features, rows = map(int, input("Enter a value").split())
X, Y = [], []

for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])

    X.append(x)  

print(X)        