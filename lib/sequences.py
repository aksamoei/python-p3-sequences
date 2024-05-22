#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibo = [0, 1]
        for n in range(2, length):
            x = fibo[-1] + fibo[-2]
            fibo.append(x)
        print(fibo)
        


print_fibonacci(1)