"""
zadanie 6, matura 2016 pr
"""


def szyfrowanie(slowo, k):
    szyfr = ""
    for i in slowo:
        nr = ord(i) + k
        while nr > 90:
            nr -= 26
        szyfr += chr(nr)
    return szyfr


def odszyfruj(slowo, k):
    jawny = ""
    for i in slowo:
        nr = ord(i) - k
        while nr < 65:
            nr += 26
        jawny += chr(nr)
    return jawny


odp1 = []
with open("dane_6_1.txt", "r") as plik1:
    for slowo in plik1:
        slowo = slowo.strip()
        odp1.append(szyfrowanie(slowo, 107))

odp2 = []
with open("dane_6_2.txt", "r") as plik2:
    for slowo in plik2:
        slowo = slowo.strip()
        slowo = slowo.split(" ")
        odp2.append(odszyfruj(slowo[0], int(slowo[1])))

odp3 = []
with open("dane_6_3.txt", "r") as plik3:
    for line in plik3:
        line = line.strip()
        slowo1, slowo2 = line.split()
        if ord(slowo2[0]) > ord(slowo1[0]):
            k = ord(slowo2[0]) - ord(slowo1[0])
        else:
            k = ord(slowo2[0]) - ord(slowo1[0]) + 26
        if szyfrowanie(slowo1, k) != slowo2:
            odp3.append(slowo1)


with open("wyniki_6_1.txt", "w") as odp:
    for s in odp1:
        odp.write(s + "\n")

with open("wyniki_6_2.txt", "w") as odpow:
    for s in odp2:
        odpow.write(s + "\n")

with open("wyniki_6_3.txt", "w") as odpowiedz:
    for s in odp3:
        odpowiedz.write(s + "\n")