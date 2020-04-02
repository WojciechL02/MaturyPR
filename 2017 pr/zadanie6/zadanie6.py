"""
zadanie 6 matura 2017 pr
"""


def spr_wiersza(w):
    ok = True
    for i in range(160):
        if w[i] != w[319-i]:
            ok = False
            break
    return ok


dane = []
licznik2 = 0
licznik3 = 0
with open("dane.txt", "r") as plik:
    for row in plik:
        row = row.strip()
        row = row.split(" ")
        dane.append(row)


ciemny = 255
jasny = 0
# 6.1
for w in dane:
    for p in w:
        if int(p) < ciemny:
            ciemny = int(p)
        if int(p) > jasny:
            jasny = int(p)

# 6.2
for w in dane:
    if spr_wiersza(w) == False:
        licznik2 += 1

# 6.3
for x in range(200):
    for y in range(320):
        pom = True
        if y-1 >= 0:
            if abs(int(dane[x][y]) - int(dane[x][y-1])) > 128:
                licznik3 += 1
                pom = False
        if y+1 <= 319 and pom:
            if abs(int(dane[x][y]) - int(dane[x][y+1])) > 128:
                licznik3 += 1
                pom = False
        if x-1 >= 0 and pom:
            if abs(int(dane[x][y]) - int(dane[x-1][y])) > 128:
                licznik3 += 1
                pom = False
        if x+1 <= 199 and pom:
            if abs(int(dane[x][y]) - int(dane[x+1][y])) > 128:
                licznik3 += 1
                pom = False

# 6.4
max_dl = 0
for k in range(320):
    dl = 0
    dl1 = 1
    for w in range(199):
        if int(dane[w][k]) == int(dane[w+1][k]):
            dl1 += 1
        else:
            if dl1 > dl:
                dl = dl1
            dl1 = 1
    if dl > max_dl:
        max_dl = dl


with open("wyniki6.txt", "w") as odp:
    odp.write("6.1\n" + "najciemniejszy: " + str(ciemny) + "\n" + "najjaśniejszy: " + str(jasny))
    odp.write("\n\n6.2\n" + str(licznik2))
    odp.write("\n\n6.3\n" + str(licznik3))
    odp.write("\n\n6.4\n" + str(max_dl))