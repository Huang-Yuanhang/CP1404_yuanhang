from guitar import Guitar


def load_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars_to_file(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    filename = 'guitars.csv'
    guitars = load_guitars_from_file(filename)

    print("All Guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("\nGuitars Sorted by Year:")
    for guitar in guitars:
        print(guitar)

    new_guitar_name = input("\nEnter the name of the new guitar: ")
    new_guitar_year = int(input("Enter the year of manufacture: "))
    new_guitar_cost = float(input("Enter the cost: "))
    new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
    guitars.append(new_guitar)

    save_guitars_to_file(filename, guitars)
    print("\nNew guitar added and list updated!")


main()
