# categorize as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("even")
    else:
        categories.append("odd")
print(categories)

categories = [ "even" if number % 2 == 0 else "odd" for number in range(10)  ]
print(categories)