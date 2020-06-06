def fibonacci_generator():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

for i in fib:
    if i > 10000:
        break
    print('Generate: ', i)
