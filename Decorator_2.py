def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def operation(func, x):
    result = func(x)
    return result

result_1 = operation(increment, 10)
result_2 = operation(decrement, 10)

print("Result of Increment Operation: ",result_1)
print("Result of Decrement Operation: ", result_2)