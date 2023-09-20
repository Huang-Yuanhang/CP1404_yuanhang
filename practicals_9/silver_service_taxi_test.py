from silver_service_taxi import SilverServiceTaxi


def main():
    my_fancy_taxi = SilverServiceTaxi("Flash 1", 100, 2)
    my_fancy_taxi.drive(18)
    print(my_fancy_taxi)
    print(f"Current fare is: ${my_fancy_taxi.get_fare():,.2f}")
    my_fancy_taxi.start_fare()
    my_fancy_taxi.drive(100)
    print(my_fancy_taxi)
    print(f"Current fare is: ${my_fancy_taxi.get_fare():,.2f}")


main()
