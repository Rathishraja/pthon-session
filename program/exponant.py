def exp(base,pow):
    result = 1
    for index in range(pow):
     result = result*base
    return result
print(exp(2,3))
