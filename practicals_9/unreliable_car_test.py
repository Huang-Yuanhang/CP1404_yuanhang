from unreliable_car import UnreliableCar


def main():
    my_ok_car = UnreliableCar(name="OK car", fuel=100, reliability=80)
    my_bad_car = UnreliableCar(name="Bad car", fuel=100, reliability=30)
    print(f"Test driving {my_ok_car.name} and {my_bad_car.name} for 5km, 10 times:")
    for i in range(0, 10):
        print(f"Attempt {i}:")
        print(f"{my_ok_car.name} drove {my_ok_car.drive(5)} km")
        print(f"{my_bad_car.name} drove {my_bad_car.drive(5)} km")
    print("The final state of both cars is:")
    print(my_ok_car)
    print(my_bad_car)


main()
