# PYTHON FONTCHECK
Grundsätzliche Unterschedung zwischen Anwendung in Produktion und nach Export

## Outline - Samuel
- Pfade geschlossen?
- Pfadrichtung?
- Extrempunkte gesetzt
- Leere Glyphen? (Soll Form enthalten/Soll keine Form enthalten (bspw. Spaces))

## Charset Check - Sophia
- (...) fehlt (Minimal Anforderung, Basic Standard)
- Was geht über den Standard hinaus?
- Prüfung über Booleans
- Abgleich mit Sprachliste
- Standardziffernsätze (Versal/Proportional)

## Vertikale Metriken - Johanna/Lennart
- Mindestens mal Output (Konsistenz über Master prüfen)
- Gegenrechnen (Max), 
- Diacritics auf jeden Fall mit einbeziehen
    
## Spacing Check - Philipp
- Dezimalprüfung (Spacing nur in 10er Schritten)
- Threshold: Sticht was raus?
- Breite des Leerzeichens (Whitespace)
    
## Kerning Check - Sophia
- Liste Ausgeben (+ Paare, - Paare)
- Überlappungs-Alarm (Boolean auf Pfade?)

## Sonstiges - Samuel
- Units für Textschriften/Displayschriften
- Sind Combs richtig angelegt?
- OT-Feature Report
- OT-Feature Bug-Report ?
- Export Report
    - Formate, Instanzen, Stammdicken (Grauwertanstieg)
- Namenlänge Checker (kommt eh nicht drüber aber könnte interessant zu programmieren sein)
- Benennung der Schriftschnitte + Foundrykürzel
- Subsetting/Fallback Fonts (Panose)
