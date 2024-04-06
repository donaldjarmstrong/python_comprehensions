# generator comprehension
#   returns values when needed

import timeit

def optimal():
    sum(x**2 for x in range(1000000))

def sub_optimal():
    sum([x**2 for x in range(1000000)])

sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)

# innefieicnt, because we preprecate the list before sum
sum_of_squares = sum([x**2 for x in range(1000000)])
print(sum_of_squares)

timer = timeit.Timer(lambda: optimal())
elapsed = timer.timeit(1)
print(f'optimal Time taken: {elapsed:.6f} seconds')

timer = timeit.Timer(lambda: sub_optimal())
elapsed = timer.timeit(1)
print(f'sub_optimal Time taken: {elapsed:.6f} seconds')
