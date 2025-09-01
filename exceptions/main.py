import basicexceptions

iterable_arg = [2, 4, 1, 9, 6]
non_iterable_arg = 12

print("\n------------ With Iterable -------------\n")
basicexceptions.crazy_iterator(iterable_arg)
print("\n------------ Without Iterable -------------\n")
basicexceptions.crazy_iterator(non_iterable_arg)

print("\n------------ Impossible Quotient -------------\n")
basicexceptions.simple_quotient(4, 0)

print("\n------------ No Age :( -------------\n")
basicexceptions.no_wrongs_in_age(-7)