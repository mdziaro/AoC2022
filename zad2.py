plik = open("input2.txt")
dane = plik.readlines()
plik.close()
WYBOR = [0,"A","B","C","A","B","C"]
ODP = [0,"X","Y","Z","X","Y","Z"]


for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]
    dane[i] = dane[i].split(" ")
print(dane)
suma = 0

for i in range(len(dane)):
    if WYBOR.index(dane[i][0]) == ODP.index(dane[i][1]):
        suma += 3+ODP.index(dane[i][1])
    elif WYBOR.index(dane[i][0]) == ODP.index(dane[i][1])-1 or WYBOR.index(dane[i][0]) == ODP.index(dane[i][1])+2:
        suma += 6+ODP.index(dane[i][1])
    elif WYBOR.index(dane[i][0]) == ODP.index(dane[i][1])+1 or WYBOR.index(dane[i][0]) == ODP.index(dane[i][1])-2:
        suma += ODP.index(dane[i][1])
print(suma)

suma = 0
for i in range(len(dane)):
    if dane[i][1] == "X":
        suma += WYBOR.index(WYBOR[(WYBOR.index(dane[i][0])+2)])
    elif dane[i][1] == "Y":
        suma += 3+WYBOR.index(WYBOR[(WYBOR.index(dane[i][0]))])
    elif dane[i][1] == "Z":
        suma += 6+WYBOR.index(WYBOR[(WYBOR.index(dane[i][0])+1)])
print(suma)

