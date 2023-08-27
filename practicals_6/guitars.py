from guitar import Guitar

guitars = []
print("My guitars!")

while True:
    guitar_name = input("Name: ")
    if guitar_name == "":
        break
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $ "))

    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

max_guitar_length = max([len(guitar.name) for guitar in guitars])

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_guitar_length}} ({guitar.year}),"
          f" worth $ {guitar.cost:10,.2f} {vintage_string}")
