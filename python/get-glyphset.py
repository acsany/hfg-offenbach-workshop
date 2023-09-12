from fontTools.ttLib import TTFont

FONTPATH = "fonts/PlayfairDisplay-Medium.ttf"

font = TTFont(FONTPATH)
glyphset = font.getGlyphSet()
for glyph in glyphset:
    print(glyph)
print(len(glyphset))
