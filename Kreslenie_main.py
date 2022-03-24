import tkinter #importuje tkinker
from random import * #importuje random
canvas = tkinter.Canvas(width=600, height=500, bg='white')#Vytvorí nám to grafikcé okno
canvas.pack()#Vlastne vloží wigety do riakov aj slpcov 
pocty = [0]*16#Je to premenná v ktorej sa 0 vypíše 16-krát 
maxy = 500# Je to premenná ktorá sa rovná 500
def kresli():#Je to definícia ktorá nesie názov kresli
canvas.delete('stlpce')#príkaz ktorý nám vymaže slpce
canvas.delete('popis')#Príkaz na vymazávanie popisu 
percenta = [0]*16# Premenná s názvom percenta v ktorej sa 0 vypíše 16-krát 
pocet_hodov_zrealizovany = sum(pocty)# Je to premenná s názvom pocet_hodov_zrealizovany ktorá sa vlastne rovná súčtu všetkých čísel v premenne pocty 
i = 0#premenná ktorá je rovná 0
for hodnota in pocty:#Vykoná akciu pre hodnota z premennej pocty
percenta[i] = hodnota / pocet_hodov_zrealizovany * 100#Premenná percenta[i] je rovná premennej hodnota deleno pocet_hodov_zrealizovaných krát 100
i += 1#Premenná i zväčšuje svoju hodnotu o 1
for i in range(16):#Vlastné vykoná akciu 16 krát 
canvas.create_rectangle(50+i*30, maxy-50, 50+i*30+20, maxy-50-pocty[i]fill='#4cb050')#Vytvorí nám obdlžník
percento = '{:.1f}%'.format(percenta[i])#Vypíše nám to percenta z percenta[i]
canvas.create_text(50+i*30+10, maxy-50-pocty[i]-20, text=percento,
tags='popis', angle=90)#Vytvorí nám to text

def simulacia():#Definícia ktorá nesie názov simulacia
global pocet_hodov, pocty#Sú to vlastne globalné premenny 
pocet_hodov -= 1#Od premennej pocet_hodov sa odčíta 1
sucet = 0# Táto premenná má hodnotu 0
for i in range(3):#Akcia sa vykoná 3-krát
hod = randint(1, 6)#Premenná hod si vyberie náhodne od 1 do 6
sucet += hod#Hodnota premeny sucet sa zvýši o hod 


pocty[sucet-3] += 1#Od premennej sucet sa odčíta 3 a prírata sa 1
kresli()#Privoláme funkciu kresli
if pocet_hodov > 0:#Podmienka že ak je pocet_hodov menší ako 0
canvas.after(10, simulacia)#Tak program počká 10 ms a zavolá si funkciu simulacia
def start():#Defínicia start
global pocet_hodov, maxy#Globálne premenny
pocet_hodov = int(entry1.get())#pocet_hodov sa rovná premennej entryl.get
maxy = pocet_hodov//5+50#Premenná maxy získa svoju hodnotu z výpočtu pocet_hodov deleno 5+50  
canvas['height'] = maxy#height sa rovná maxy
for i in range(16):# Vykoná túto čast programu 16-krát
canvas.create_text(50+i*30+10, maxy-30, text=str(i+3))#Vytvorí sa text 
simulacia()#program privolá funkciu simulacia
label1 = tkinter.Label(text='Počet hodov:')# Táto premenná vytvorí text 
label1.pack()#Zobrazí nam text
entry1 = tkinter.Entry()#Vytvorí text na prijímanie hodnôt od uživateľa
entry1.pack()#Zobrazí nám to entry1
button1 = tkinter.Button(text='štart', command=start)#Príkaz nám vytvorí tlačidlo 
button1.pack()#Zobrazí sa nám tlačidlo 
pocet_hodov = 0# Hodnota premennej je 0