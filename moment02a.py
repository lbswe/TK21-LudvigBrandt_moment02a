#Ludvig Brandt, TK21
#Moment02, inlämningsuppgift 1
# Enligt mig så var grunderna med denna uppgift ganska simpel alltså
# Enhet, radie, pi, area etc.
# Det svåra var att kunna avrunda och skriva ut "if" och "else" printsen.
# Dino hjälpte till med grunderna men jag kunde resten
enhet = "cm\u00b2"

radie = float(input('Vad är den exakta Radien på Cirkeln?'))

pi = 3.14

omkrets = float(2*pi*radie)

area = pi*radie**2

Radieinteger = int(radie), enhet

Areainteger = int(pi*radie**2), enhet

Omkretsinteger = int(omkrets)

avradie = round(radie, 2), enhet # 1 utan avradie,avarea,avomkrets så kan man inte ha med decimaltal.

avarea = round(area, 2), enhet

avomkrets = round(omkrets, 2), enhet

if float(radie).is_integer():
        print('area:{0} radie:{1}omkrets:{2}'.format(Areainteger, Radieinteger, Omkretsinteger))
else:
        print('area:{0} radie:{1}omkrets: {2}'.format(avarea, avradie, avomkrets))
1