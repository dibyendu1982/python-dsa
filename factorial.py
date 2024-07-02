def factorial(value):
    if value == 0 :
        return 1
    result = value * factorial(value-1)
    return result

print(factorial(5))


    