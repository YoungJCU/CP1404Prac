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

COLOR_TO_CODE_LOWER={key.lower(): COLOR_TO_CODE[key]for key in COLOR_TO_CODE.keys()}
color_code = input("Enter color: ").strip().lower()
while color_code != "":
    try:
        print(color_code, "is", COLOR_TO_CODE_LOWER[color_code])
    except KeyError:
        print("Invalid color")
    color_code = input("Enter color: ").strip().lower()