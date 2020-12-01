#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program calculates sum from
#   inputted variables


def main():
    # this function calculates sum

    # input
    first = int(input("Enter first number:"))
    second = int(input("Enter second number:"))

    # process
    sum = first+second

    # output
    print("")
    print("{} + {} = {}".format(first, second, sum))


if __name__ == "__main__":
    main()
