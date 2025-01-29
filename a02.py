#*****************************************************************************
# Author:       	Ari P.
# Assignment:       Assignment 2
# Date:         	1/29/2025
# Description:  	This program will prompt the user for a year after 1582
#                   and determine if it’s a leap year. It will also calculate
#                   how long ago, or how far in the future, the given year is.
# Input:        	Year (int)
# Output:       	Welcome message (string), input prompt (string), error
#                   message (string), result message (string), goodbye message
#                   (string), distance from year (int)
# Sources:      	Assignment 2 specifications, assignment 2 sample, python
#                   style guide, unit 4 python practice problems, W3Schools
#                   python reference, method to determine whether a year is a
#                   leap year (Microsoft Learn)
#*****************************************************************************

def main():
    # Create variables
    year = 0
    yearDifference = 0
    leapYear = False

    # Print welcome message
    print("This program will calculate whether any given year after 1582 is a"
    " leap year.")

    # Prompt for year
    year = float(input("\nEnter a year after 1582: "))

    # Ensure year is valid
    year = int(year)
    if year < 1582:
        print("\nThat's not a valid year.")
    else:
        # Determine whether year is a leap year
        if year % 4 == 0 and year % 100 != 0:
            leapYear = True
        if year % 100 == 0 and year % 400 == 0:
            leapYear = True
        # Determine the year difference
        yearDifference = year - 2025
        # Print result with several grammatical variations
        if yearDifference == -1:
            print("\nLast year, ", str(year), " was ", sep="", end="")
            if leapYear == False:
                print("not a leap year.")
            else:
                print("a leap year.")
        elif yearDifference < 0:
            print("\n", str(abs(yearDifference)), " years ago, ", str(year), " was ",
            sep="", end="")
            if leapYear == False:
                print("not a leap year.")
            else:
                print("a leap year.")
        elif yearDifference == 0:
            print("\n", str(year), " is ", sep="", end="")
            if leapYear == False:
                print("not a leap year.")
            else:
                print("a leap year.")
        elif yearDifference == 1:
            print("\nNext year, ", str(year), " will ", sep="", end="")
            if leapYear == False:
                print("not be a leap year.")
            else:
                print("be a leap year.")
        else:
            print("\nIn ", str(yearDifference), " years, ", str(year), " will ",
            sep="", end="")
            if leapYear == False:
                print("not be a leap year.")
            else:
                print("be a leap year.")
    # Print goodbye message
    print("\nFeel free to try again with a different year!")

main()