# Define a constant dictionary of color names and their corresponding codes
COLORS = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antique white": "#faebd7",
    "aquamarine1": "#7fffd4",
    "azure1": "#f0ffff"
}

# Main program loop
while True:
    user_input = input("Enter a color name (or blank to quit): ").lower()

    if user_input == "":
        break

    color_code = COLORS.get(user_input, "Color not found")
    print(f"The color code for {user_input} is {color_code}")
