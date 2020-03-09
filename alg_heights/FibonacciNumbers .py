def Fibonacci_Loop(number):
    old = 1
    new = 1
    for itr in range(number - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new


def Fibonacci_Loop_Pythonic(number):
    old, new = 1, 1
    for itr in range(number - 1):
        new, old = old, old + new
    return new


print(Fibonacci_Loop(13))
print(Fibonacci_Loop_Pythonic(13))
