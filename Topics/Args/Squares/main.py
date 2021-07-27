def sq_sum(*args):
    args = list(map(lambda x: x ** 2, args))
    return sum(args)
