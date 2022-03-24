
cislo= int(input("Zadajte cislo :"))
if(cislo%3 == 0 and cislo%10 == 8 ):
  print("Cislo je delitelne 3")
  print("Cislo ma na konci 8")


cislo = input("Zadajte rodne cislo : ")
order = cislo[2:4]
if len(cislo) == 10:
  cislo = int(cislo)
  over = cislo / 11
if cislo.is_integer():
    cislo = str(cislo)
if order == "01" or "51" or "02" or "52" or "03" or "53" or "04" or "54" or "05" or "55" or "06" or "56" or "07" or "57" or "08" or "58" or "09" or "59" or "10" or "60" or "11" or "61" or "12" or "62":
 print("rodné číslo je valídne")

 
entry= str(input("Vyberte si prevod na f- Frenheit a k - Kelvin :"))
teplota = int(input("Zadaj teplotu :"))
if entry == "k":
  kelvin = teplota + 273.15
  print ("Teplota v Kelvinoch je :",kelvin)
elif entry == "f":
  farenheit = teplota * 1.8
  print("Teplota v Kelvinoch je :",farenheit)

