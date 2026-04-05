# Daily Schedule Tracker
# Gemaakt door: Marc Brouwer
# Doel: Dagelijkse checklist voor medicijnen en huisdieren

import datetime

nu = datetime.datetime.now()
print("=== Dagelijkse Checklist ===")
print("Datum:", nu.strftime("%d-%m-%Y"))
print("Tijd:", nu.strftime("%H:%M:%S"))
print("")
print("heb je je Esomeprazol al ingenomen?")
esomeprazol = input("(j/n): ")

if esomeprazol == "j":
    print("Top! Zet een timer voor 1 uur.")
else:
    print("Vergeet het niet! Nuchter innemen!")
print("MEDICIJNEN OCHTEND:")
print("  [ ] Esomeprazol innemen (nuchter!)")
print("  [ ] 1 uur wachten...")
print("  [ ] ontbijt + 2x Metformine + 1x Gliclazide")
print("")
print("HUISDIEREN:")
print("  [ ] Kattenbakken verschonen + Cat Box Fresh")
print("  [ ] Cavia Kooien: natte plekken + bijvullen")
print("  [ ] Water en voer checken")
print("")
print("MEDICIJNEN AVOND:")
print("  [ ] Avondeten + 2x Metformine")