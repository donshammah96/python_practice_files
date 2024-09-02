name = input("camelCase: ")
new_name = ""

if name[0].isupper():
    new_name += name[0].lower()
else:
    new_name += name[0]


for char in name[1:]:
    if char.isupper():
        new_name += "_" + char.lower()
    else:
        new_name += char.lower()

print(f"snake_case: {new_name}")