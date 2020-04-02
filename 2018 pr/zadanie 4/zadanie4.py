"""
zadanie 4, matura 2018 pr
"""


def rozne_litery(n):
    il = 0
    lista = []
    for E in n:
        if E not in lista:
            lista.append(E)
            il += 1
    return il


def rozne_litery_slowo(n):
    il = 0
    lista = []
    slowo = n
    for E in n:
        if E not in lista:
            lista.append(E)
            il += 1
    return slowo


def odleglosc(n):
    ok = True
    m = 0
    while m <= len(n)-1:
        for k in range(0, len(n)):
            if abs(alfabet.get(n[m]) - alfabet.get(n[k])) > 10:
                ok = False
                break
        m += 1
    return ok


lista1 = []
max2 = 0
slowo2 = ""
lista3 = []
alfabet = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
with open("sygnaly.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        lista1.append(L)
        # 4.2
        if rozne_litery(L) > max2:
            max2 = rozne_litery(L)
            slowo2 = rozne_litery_slowo(L)
        # 4.3
        if odleglosc(L):
            lista3.append(L)

# 4.1
odp1 = ""
i = 39
while i <= 1000:
    pom = lista1[i]
    odp1 += pom[9]
    i += 40

with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + odp1)
    odp.write("\n\n4.2\n" + str(max2) + "  " + slowo2)
    odp.write("\n\n4.3\n")
    for E in lista3:
        odp.write(E + "\n")
