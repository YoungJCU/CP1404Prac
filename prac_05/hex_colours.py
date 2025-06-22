COLOR_TO_CODE= {
"Absolute Zero": "#0048ba",
"Acid Green": "#b0bf1a",
"AliceBlue": "#f0f8ff",
"Alizarin crimson": "#e32636",
"Amaranth": "#e52b50",
"Amber": "#ffbf00",
"Amethyst": "#9966cc",
"AntiqueWhite": "#faebd7",
"AntiqueWhite1": "#ffefdb",
"AntiqueWhite2": "#eedfcc",
"AntiqueWhite3": "#cdc0b0"}
name_width=max((len(name) for name in COLOR_TO_CODE))

print("\n".join([f"{name:{name_width}} is {value}"for name,value in COLOR_TO_CODE.items()]))

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", COLOR_TO_CODE[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper