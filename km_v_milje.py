# -*- encoding: utf-8 -*-
print ("Pozdravljeni v pretvorniku kilometrov v milje")

km = float(raw_input("Vnesite kilometre: "))
milje = km * 0.62137
print(milje)

vprasaj = raw_input("Ali želite narediti novo pretvorbo da/ne? ").lower()

while vprasaj == "da":
    km = float(raw_input("Vnesite kilometre: "))
    milje = km * 0.62137
    print(milje)
    vprasaj = raw_input("Ali želite narediti novo pretvorbo da/ne? ").lower()
if  vprasaj == "ne":
    print "Lep pozdrav."