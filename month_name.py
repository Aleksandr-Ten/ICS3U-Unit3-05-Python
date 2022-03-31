#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells the user the name of the month with user inputs number


def main():
    # this function tells the user the name of the month

    # input
    month_number = int(input("Enter the month number(ex: 3 for March):"))
    print("")

    # process and output
    if month_number == 1:
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("Incorrect month number!")


if __name__ == "__main__":
    main()
