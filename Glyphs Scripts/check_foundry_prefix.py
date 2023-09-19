Glyphs.clearLog()
foundry_prefix = "Off"
family_name = Glyphs.font.familyName

print(f"Family Name is: {family_name}")
print("---")

# Foundry Prefix must be present somewhere in the family name
if foundry_prefix in family_name:
    print("Family name is correct!")
else:
    print("Family name is wrong!")

print("---")

# Foundry name must be at the beginning and contain a space after it
if family_name.startswith(foundry_prefix + " "):
    print("Family name is correct!")
else:
    print("Family name is wrong!")
