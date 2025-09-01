
def simple_quotient(num, divisor):
    try:
        quotient = num / divisor
    except ZeroDivisionError:
        print("Divisor cannot be 0!!\nEXITING...")
        #print("Divisor cannot be 0!!")
        return
    return (quotient)


def crazy_iterator(iterable_param):
    try:
        count = 0
        while True:
            print(f"Item {count} is: {iterable_param[count]}")
            count += 1
    except TypeError:
        print("ERROR: iterable param must be ITERABLE!!\nEXITING...")
    except IndexError:
        print("ERROR: sequence outta bounds!!\nEXITING...")

def no_wrongs_in_age(param):
    if param <= 0:
        print("\nAge cannot be 0 or less!!\nWill EXIT after next EXCEPTION!!\n")
        raise ValueError("\nAge cannot be 0 or less!!\n")
    else:
        print(f"Are you sure you're {param} years old?!!")
