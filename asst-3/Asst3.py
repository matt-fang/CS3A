"""Download and display historical temperature information.

This package allows the user to download historical temperature
information using the open-meteo API, and display summary information.
"""


def main():
    """Take user's name and print greeting.

    :return: None
    """

    name = input("Please enter your name: ")
    print(f"Hi {name}, let's explore some historical temperatures.")

    menu()


def print_menu():
    """Print the main menu.

    :return: None"""

    main_menu = """Main Menu
1 - Load dataset one
2 - Load dataset two
3 - Compare average temperatures
4 - Dates above threshold temperature
5 - Highest historical dates
6 - Change start and end dates for dataset one
7 - Change start and end dates for dataset two
9 - Quit"""
    print("\n" + main_menu)


def menu():
    """Collect the user's menu selection.

    :return: None"""

    print_menu()
    option = input("What is your choice? ")

    try:
        option = int(option)
    except ValueError:
        print("please enter a numerical value")
        return

    if option == 1:
        print("option 1 is not functional yet")
    elif option == 2:
        print("option 2 is not functional yet")
    elif option == 3:
        print("option 3 is not functional yet")
    elif option == 4:
        print("option 4 is not functional yet")
    elif option == 5:
        print("option 5 is not functional yet")
    elif option == 6:
        print("option 6 is not functional yet")
    elif option == 7:
        print("option 7 is not functional yet")
    elif option == 8:
        print("option 8 is not functional yet")
    elif option == 9:
        print("option 9 is not functional yet")
    else:
        print("your choice is out of range")


if __name__ == "__main__":
    main()
