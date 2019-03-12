#!/usr/bin/python

# Algorithmen_Aufgabe1_ADGorki_Fibonacci numbers inefficient

import argparse

parser = argparse.ArgumentParser(description="Calculate fibonacci numbers")
parser.add_argument("input", type=int, help="integer number n")
parser.add_argument("--all", help="displays all fibonacci numbers up to n", action= "store_true")
args = parser.parse_args()

fibonumbers = [1,1]

def fibonacci(n):
    """Calculates n-th fibonacci number"""
    if n == 1 or n == 2:
        return 1
    else:
        x = fibonacci(n - 1)
        y = fibonacci(n - 2)
        fibo_num = x+y
        if fibo_num > max(fibonumbers):
            fibonumbers.append(fibo_num)
        return fibo_num

fibonacci(args.input)

if args.all == True:
    print (fibonumbers)
else:
    print (fibonumbers[args.input-1])