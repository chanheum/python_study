count = 0

def fibonacci(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for n in range(1, 10+1):
    print("fibonacci({}) = {}".format(n, fibonacci(n)))
print(count)