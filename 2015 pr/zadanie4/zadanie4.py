"""
zadanie 4, matura 2015 pr
"""


def wiecej_zer(n):
    z = 0
    j = 0
    for C in n:
        if C == "1":
            j += 1
        else:
            z += 1
    if z > j:
        return True
    else:
        return False


licznik1 = 0
przez2 = 0
przez8 = 0
max3 = 0
min3 = 100000000000000000000000000000000000000000000000
max_i = 0
min_i = 0
i = 1
with open("liczby.txt", "r") as plik:
    for L in plik:
        L = L.strip()
        # 4.1
        if wiecej_zer(L):
            licznik1 += 1
        # 4.2
        if int(L) % 2 == 0:
            przez2 += 1
        if int(L) % 8 == 0:
            przez8 += 1
        # 4.3
        if int(L, 2) > max3:
            max3 = int(L, 2)
            max_i = i
        if int(L, 2) < min3:
            min3 = int(L, 2)
            min_i = i
        i += 1


with open("wyniki4.txt", "w") as odp:
    odp.write("4.1\n" + str(licznik1))
    odp.write("\n\n4.2\n" + "Przez 2: " + str(przez2) + "\n" +
              "Przez 8: " + str(przez8))
    odp.write("\n\n4.3\n" + "Najmniejsza: " + str(min_i) + "\n" +
              "Największa: " + str(max_i))