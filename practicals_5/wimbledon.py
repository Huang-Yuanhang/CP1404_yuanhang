def wimbledon_data(filename):
    champions = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:

        for line in in_file:
            parts = line.split(",")

            if parts[0] == "Year":
                continue

            champion = parts[2]
            country = parts[1]

            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)

    return champions, countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    sorted_countries = sorted(countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(', '.join(sorted_countries))


def main():

    filename = "wimbledon.csv"
    champions, countries = wimbledon_data(filename)

    display_champions(champions)
    display_countries(countries)


main()
