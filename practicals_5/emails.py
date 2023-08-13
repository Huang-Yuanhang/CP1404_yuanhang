def extract_name(email):
    username = email.split('@')[0]
    name_parts = [part.title() for part in username.split('.')]
    return ' '.join(name_parts)


def main():
    email_name_dict = {}
    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name(email)
        correct_name_check = input(f"Is your name {name}? (Y/n) ")

        if correct_name_check.lower() != "y":
            name = input("Name: ")

        email_name_dict[email] = name

    print("\nResults:")
    for email, name in email_name_dict.items():
        print(f"{name} ({email})")


main()
