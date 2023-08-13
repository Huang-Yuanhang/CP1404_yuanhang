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

user_input = input("Enter a color name (or blank to quit): ").lower()
while user_input != "":
    color_code = COLORS.get(user_input, "Color not found")
    print(f"The color code for {user_input} is {color_code}")
    user_input = input("Enter a color name (or blank to quit): ").lower()
