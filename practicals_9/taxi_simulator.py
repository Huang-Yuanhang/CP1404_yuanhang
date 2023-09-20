from practicals_9.silver_service_taxi import SilverServiceTaxi
from practicals_9.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")

    while True:
        print(MENU)
        menu_choice = input(">>> ").lower()

        if menu_choice == "q":
            break
        elif menu_choice == "c":
            print("Taxis available:")
            display_taxis(TAXIS)
            taxi_choice = get_valid_integer("Choose taxi: ")

            if taxi_choice < 0 or taxi_choice >= len(TAXIS):
                print("Invalid taxi choice")
            else:
                current_taxi = TAXIS[taxi_choice]
        elif menu_choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_valid_integer("Drive how far? ")
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(TAXIS)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_integer(prompt):
    while True:
        try:
            integer = int(input(prompt))

            if integer < 0:
                print("Number must be >= 0")
            else:
                return integer
        except ValueError:
            print("Invalid input; enter a valid number")


main()
