# get all even numbes from 0 - 50

evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
print(evens)

evens = [ x for x in range(50) if x % 2 == 0 ]
print(evens)