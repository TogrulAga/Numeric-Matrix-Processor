n = int(input())


def even(number):
    i = 0
    for _ in range(number):
        yield i
        i += 2


# Don't forget to print out the first n numbers one by one here
even_generator = even(n)

for _ in range(n):
    print(next(even_generator))
