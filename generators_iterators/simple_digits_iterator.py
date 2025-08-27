
def simple_digits_generator(n):
    for i in range(n):
        yield i

def nos_square(num):
    for val in range(1, num + 1):
        yield val * val

def myfib(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        future = a + b
        a = b
        b = future

