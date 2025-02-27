import random
print('ELSŐ FELADAT')

gues = int(input('Találd ki a következő dobás számát ha ki gondoltad akkor írd be 0-6ig'))
dobas = random.randint(0,6)
if dobas == gues:
     print('Eltaláltad, ügyes vagy!')
else:
    print('Majd kövire sikerülni fog talán...')
print('A random dobás eredménye:',dobas)
    
print('MÁSODIK FELADAT')

guide = input('írd be azt hogy "random" ha szeretnél generálni egy random számot a listádba')
if guide == ('random'):
    print('már is adom')
else:
    print('kezdjed elfele írni mert rosszba leszünk')
    
eredmenyeklista = []
eredmeny = random.randint(0,6)
print(eredmeny)
eredmenyeklista.append(eredmeny)
akarat = input('írd be azt hogy "szeretném" ha szeretnéd ki iratni az eredményt tartalmazó listát')
if akarat == ('szeretném'):
    print(eredmenyeklista)
else:
    print('szólj ha meggondoltad magad')




print('HARMADIK FELADAT')
eredmenyek3f = []

gues1 = input('írd be hogy p1')

if gues1 == ('p1'):
    print('köszönöm')
else:
    print('miért nem csinálod azt amit mondtam?')
    
gues1 = random.randint(0,6)
print(gues1)
print('Ez volt az első szám.')
eredmenyek3f.append(gues1)

gues2 = input('írd be hogy p2')

if gues2 == ('p2'):
    print('köszönöm')
else:
    print('miért nem csinálod azt amit mondtam?')

gues2 = random.randint(0,6)
print(gues2)
print('Ez volt az második szám.')

eredmenyek3f.append(gues2)

gues3 = input('írd be hogy p3')

if gues3 == ('p3'):
    print('köszönöm')
else:
    print('miért nem csinálod azt amit mondtam?')

gues3 = random.randint(0,6)
print(gues3)
print('Ez volt az harmadik szám.')

eredmenyek3f.append(gues3)

print('ez a 3 eredmény áll a listádban:',eredmenyek3f)


végeredmény = input('Ha kíváncsi vagy hogy ki nyert akkor írd be hogy "győztes?"')
if végeredmény == ('győztes?'):
    print('akkor mondom is')
else:
    print('Így soha sem fogod meg tudni hogy ki nyert jobban jársz ha kideríted és beírod hogy "győztes?"')

print('A nyertes nem más mint')

if gues1 + gues2 + gues3>=10:
    print('Te,','A krupié vesztett, Te pedig nyertél, tessék itt egy százas.')
else:
    print('Krupié,','A krupié nyert, Te pedig esztettél, adj egy százast.')
    
