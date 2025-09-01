"""
    What parameters should be sent to the range constructor, to produce a
    range with values 50, 60, 70, 80?
"""
ranger = range(50, 90, 10)

def func():
    try:
        #next(ranger)
        #print(i for i in next(ranger))
        for i in range(50, 90, 10):
            print(f"{i} ")
    except Exception as e:
        print(e)

func()