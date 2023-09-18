# PYTHON FONTCHECK
Grundsätzliche Unterschedung zwischen Anwendung in Produktion und nach Export

## Outline
- Pfade geschlossen?
- Pfadrichtung?
- Extrempunkte gesetzt
- Leere Glyphen? (Soll Form enthalten/Soll keine Form enthalten (bspw. Spaces))

## Charset Check
- (...) fehlt (Minimal Anforderung, Basic Standard)
- Was geht über den Standard hinaus?
- Prüfung über Booleans
- Abgleich mit Sprachliste
- Standardziffernsätze (Versal/Proportional)

## Vertikale Metriken
- Mindestens mal Output (Konsistenz über Master prüfen)
- Gegenrechnen (Max), 
- Diacritics auf jeden Fall mit einbeziehen
    
## Spacing Check
- Dezimalprüfung (Spacing nur in 10er Schritten)
- Threshold: Sticht was raus?
- Breite des Leerzeichens (Whitespace)
    
## Kerning Check
- Liste Ausgeben (+ Paare, - Paare)
- Überlappungs-Alarm (Boolean auf Pfade?)

## Sonstiges
- Units für Textschriften/Displayschriften
- Sind Combs richtig angelegt?
- OT-Feature Report
- OT-Feature Bug-Report ?
- Export Report
    - Formate, Instanzen, Stammdicken (Grauwertanstieg)
- Namenlänge Checker (kommt eh nicht drüber aber könnte interessant zu programmieren sein)
- Benennung der Schriftschnitte + Foundrykürzel
- Subsetting/Fallback Fonts (Panose)
