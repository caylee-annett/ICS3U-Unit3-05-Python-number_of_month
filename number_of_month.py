#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints the month that matches the integer that
#   the user entered


def main():
    # This function tells the user which month matches their number

    # Input
    number_of_month = int(input(
        "Enter the number of a month (ex. 4 for April): "))
    print("")

    # Process & Output
    if number_of_month == 1:
        print("Month #1 is January.")
    elif number_of_month == 2:
        print("Month #2 is February.")
    elif number_of_month == 3:
        print("Month #3 is March.")
    elif number_of_month == 4:
        print("Month #4 is April.")
    elif number_of_month == 5:
        print("Month #5 is May.")
    elif number_of_month == 6:
        print("Month #6 is June.")
    elif number_of_month == 7:
        print("Month #7 is July.")
    elif number_of_month == 8:
        print("Month #8 is August.")
    elif number_of_month == 9:
        print("Month #9 is September.")
    elif number_of_month == 10:
        print("Month #10 is October.")
    elif number_of_month == 11:
        print("Month #11 is November.")
    elif number_of_month == 12:
        print("Month #12 is December.")
    else:
        print("Not a month.")
    print("\nDone.")


if __name__ == "__main__":
    main()
