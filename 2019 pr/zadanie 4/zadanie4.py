"""
zadanie 4, matura 2019 pr
"""


def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n-1) * n


def suma_silni(x):
    suma = 0
    while x > 0:
        suma += silnia(x % 10)
        x = x // 10
    return suma


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


lista = []
lista3 = []
odp2 = []
licznik1 = 0
for n in range(0, 11):
    lista.append(pow(3, n))
with open("liczby.txt", "r") as plik:
    for L in plik:
        L = int(L.strip())
        lista3.append(L)
        # 4.1
        if L in lista:
            licznik1 += 1
        # 4.2
        if L == suma_silni(L):
            odp2.append(L)
# 4.3
N = len(lista3)
dzielmax = 0
dlmax = 0
pierwszamax = 0
for i in range(N-1):
    dl = 1
    pierwsza = lista3[i]
    localnwd = lista3[i]
    for j in range(i+1, N):
        n = NWD(localnwd, lista3[j])
        if n > 1:
            dl += 1
            localnwd = n
        if n == 1 or j == N-1:
            if dlmax < dl:
                dlmax = dl
                pierwszamax = pierwsza
                dzielmax = localnwd
            break


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + str(licznik1))
    odp.write("\n\n4.2\n" + str(odp2))
    odp.write("\n\n4.3\n" + str(pierwszamax) + " " + str(dlmax) + " " + str(dzielmax))