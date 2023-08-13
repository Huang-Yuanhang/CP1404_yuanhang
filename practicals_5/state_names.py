"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_CODES_TO_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(STATE_CODES_TO_NAMES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state_name = STATE_CODES_TO_NAMES[state_code]
        print(f"{state_code:3} is {state_name}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

print("\nAll states and names:")

for code, name in STATE_CODES_TO_NAMES.items():
    print(f"{code:3} is {name}")
