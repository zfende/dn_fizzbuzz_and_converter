# -*- encoding: utf-8 -*-
print ("Pozdravljeni v pretvorniku kilometrov v milje in obratno")
izbor = int(raw_input("Če želite pretvarjati kilometre v milje izberite št. 1, za milje v kilometre izberite št. 2. Izberi: "))


while izbor == 1:
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
        break

while izbor == 2:
    milje = float(raw_input("Vnesite milje: "))
    km = milje * 1.609344
    print(km)

    vprasaj = raw_input("Ali želite narediti novo pretvorbo da/ne? ").lower()

    while vprasaj == "da":
        milje = float(raw_input("Vnesite milje: "))
        km = milje * 1.609344
        print(km)
        vprasaj = raw_input("Ali želite narediti novo pretvorbo da/ne? ").lower()
    if  vprasaj == "ne":
        print "Lep pozdrav."
        break