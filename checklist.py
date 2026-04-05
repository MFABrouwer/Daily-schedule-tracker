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
print("  [ ] Kattenbakken verschonen + Cat Box Fresh")
print("  [ ] Cavia Kooien: natte plekken + bijvullen")
print("  [ ] Water en voer checken")
print("")
print("MEDICIJNEN AVOND:")
print("  [ ] Avondeten + 2x Metformine")