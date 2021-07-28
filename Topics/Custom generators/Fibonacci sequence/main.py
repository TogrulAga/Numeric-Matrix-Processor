def fibonacci(n):
    previous = 0
    before_previous = 0

    for i in range(n):
        next_element = previous + before_previous
        yield next_element
        before_previous = previous if i != 1 else 0
        previous = next_element if next_element != 0 else 1
