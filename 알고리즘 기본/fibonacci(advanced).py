dictionary = {
    1:1,
    2:1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output  # 메모화
        return output

print("fibonacci(10) : {}".format(fibonacci(10)))
print("fibonacci(10) : {}".format(fibonacci(20)))
print("fibonacci(10) : {}".format(fibonacci(30)))
print("fibonacci(10) : {}".format(fibonacci(40)))
print("fibonacci(10) : {}".format(fibonacci(50)))
