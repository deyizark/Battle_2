import random

print()
print("Byenvini nan pwogram epsedo sosyal nou an")
print()

non = input("Rantre non w silvouplè : ").title()
siyati = input("Mete siyati w silvouplè : ").title()

try :
    data = open("database.txt", "r")
    data.close()
except FileNotFoundError:
    data = open("database.txt", "w")
    data.close()

kantite = 0
data = open("database.txt", "r")
da_ta_ba_se = data.read().split(",")

data.close()
kantite = len(da_ta_ba_se) - 1
print()
print(f"Bonjou {non.title()} {siyati.title()}, nou rekoni nan sèvis nou an ")
if kantite > 0:
    print(f"Nou deja jenere epsedo pou {kantite} moun deja")

lis_non = non.split() + siyati.split()

epsedo1 = ""
for no_n in lis_non:
    epsedo1 += no_n[0].upper()

epsedo1 += str(len("".join(lis_non)))

epsedo2 = "".join(lis_non).title() 

#print(epsedo1)

#print(epsedo2)

#print(epsedo3)

lis_len =[]
for i in lis_non:
    lis_len.append(len(i))

endis = lis_len.index(min(lis_len))

epsedo3 = lis_non[endis][::-1].capitalize() + str(random.randrange(100,1000))
lis_epsedo = [non,siyati,epsedo1,epsedo2,epsedo3]

lisepsedo7 = []

for e in lis_epsedo:
    if len(e) < 7:
        lisepsedo7.append(e)

#print(lisepsedo7)

chwa = random.choice(lisepsedo7)
data = open("database.txt", "a")
data.write(chwa + ",")
data.close()

print()
print(f"Apre tout kalkil {chwa} se yon bon epsedo ou ka itilize sou rezo w yo")
print()
print(f"Bye {non.title()} nou te kontan genyen w kòm itilizatè !!!")
print()