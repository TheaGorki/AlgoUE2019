#!/usr/bin/python

# Algorithmen_Aufgabe2_ADGorki_TowersOfHanoi

import argparse
import sys

parser = argparse.ArgumentParser(description="Tower of Hanoi problem")
parser.add_argument("-n", type=int, help="integer number n")
args = parser.parse_args()

def hanoitowers(n,pegstart =1,pegende=3):
    """Resolve problem of hanoi towers"""
    global countsteps
    if n == 1:
        print("Move disk from peg {} to peg {}.".format(pegstart, pegende))
        countsteps += 1
        return
    unusedpeg = 6 - pegstart - pegende
    hanoitowers(n-1, pegstart, unusedpeg)
    print("Move disk from peg {} to peg {}.".format(pegstart, pegende))
    countsteps += 1
    hanoitowers(n-1, unusedpeg, pegende)
    return

countsteps = 0

hanoitowers(args.n)

sys.stderr.write("The number of steps needed is {0}.\n".format(countsteps))


