import simple_digits_iterator as sdi

print("Simple Digits:")
for digit in sdi.simple_digits_generator(5):
    print(digit)

print("Num Squares:")
for square in sdi.nos_square(5):
    print(square)

print("Fibonacci Sequence:\n--------------------\n")
fib_7 = sdi.myfib(7)
next(fib_7)
next(fib_7)
print(f'\tSingle fib(3rd): {next(fib_7)}')
next(fib_7)
print("\n\tMore Fib sequence:")
while True:
    try:
        print(f'\t\tNext fib: {next(fib_7)}')
    except StopIteration:
        break
