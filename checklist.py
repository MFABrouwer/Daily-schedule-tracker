# Daily Schedule Tracker
# Gemaakt door: Marc Brouwer
# Doel: Dagelijkse checklist voor medicijnen en huisdieren

import datetime

nu = datetime.datetime.now()
print("=== Dagelijkse Checklist ===")
print("Datum:", nu.strftime("%d-%m-%Y"))
print("Tijd:", nu.strftime("%H:%M:%S"))
print("")
print("MEDICIJNEN OCHTEND:")
print("heb je je Esomeprazol al ingenomen?")
esomeprazol = input("(j/n): ")
if esomeprazol == "j":
    print("  [x] Esomeprazol nuchter ingenomen")
    print("  Top zet een timer voor 1 uur.")
else:
    print("  [ ] Esomeprazol innemen (nuchter!)") 
    print("  Vergeet het niet! Nuchter innemen!")
print("  [ ] 1 uur wachten...")
ontbijt = input("Ontbijt + Medicijnen genomen? (j/n): ")
if ontbijt == "j":
    print("  [x] Ontbijt + 2x Metformine + 1x Gliclazide")
else:
    print("  [ ] Ontbiijt + 2x Metformine + 1x Gliclazide")
print("")
print("HUISDIEREN:")
kattenbak = input("Kattenbakken verschoond? (j/n): ")
if kattenbak == "j":
    print("  [x] Kattenbakken verschonen + Cat Box Fresh")
else:
    print("  [ ] Kattenbakken verschonen + Cat Box Fresh")

kooien = input("Cavia kooien gedaan? (j/n): ")
if kooien == "j":
    print("  [x] Cavia kooien: natte plekken + bijvullen")
else:
    print("  [ ] Cavia kooien: natte plekken + bijvullen")

voer = input("Water en voer gecheckt? (j/n): ")
if voer == "j":
    print("  [x] Water en voer checken")
else:
    print("  [ ] Water en voer Checken")
print("")
print("MEDICIJNEN AVOND:")
print("  [ ] Avondeten + 2x Metformine")