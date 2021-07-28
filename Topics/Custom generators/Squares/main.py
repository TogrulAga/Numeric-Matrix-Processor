n = int(input())


def squares():
    i = 1
    while True:
        yield i ** 2
        i += 1


# Don't forget to print out the first n numbers one by one here
square_yielder = squares()
for j in range(n):
    print(next(square_yielder))
