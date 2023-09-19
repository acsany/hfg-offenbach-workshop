Glyphs.clearLog()
f = Glyphs.font

# Check Glyphs Python Doc for more values to check: https://docu.glyphsapp.com/#GSFont
font_values = {
    # Name: (value, expected_value)
    "UPM Size": (f.upm, 1000),
    "Family Name": (f.familyName, "Off Blurr")
}

for name, (value, expected_value) in font_values.items():
    if value == expected_value:
        print(f"✅ {name} is: {value}")
    else:
        print(f"❌ {name} is: {value} (but should be: {expected_value})")
