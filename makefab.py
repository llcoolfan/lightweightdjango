#!/usr/bin/python3
# -*- coding=utf-8 -*-
# author : llcoolf

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(f'fib(10)={fib(10)}')
    print(f'fib(13)={fib(13)}')
