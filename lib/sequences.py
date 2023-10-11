#!/usr/bin/env python3

def print_fibonacci(length):
    

    if length == 0:
        fib_list = []
    elif length == 1:
        fib_list = [0]
    elif length == 2:
        fib_list = [0,1]
    else:
        fib_list = [0,1]
        while len(fib_list) < length:
            next_sum = fib_list[-1] + fib_list[-2]
            fib_list.append(next_sum)

    print(fib_list) 

    