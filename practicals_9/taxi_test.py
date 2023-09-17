from taxi import Taxi


def main():

    my_taxi = Taxi(name="Prius 1", fuel=100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare is: ${my_taxi.get_fare():,.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare is: ${my_taxi.get_fare():,.2f}")


main()
