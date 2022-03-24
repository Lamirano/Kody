import time
while True:
  print('\x1bc')
  print("Vítajte v menu prajeti si pokračovať ? Ak chcete pokračovať stlačte 1 ak nie tak 2")
  vstup=int(input("Zadajte svoju voľbu :"))
  if vstup==1:
    print("Nech sa vám páči")
  else:
    print("Dovidenia :)")
    exit()
  vstup1=input("\nZadaj svoje meno :")
  print("Vítajte",vstup1,"\nv programe na vypočet Vášho veku,ktorý Vám aj určí koľko rokov Vám zostáva do dôchodku,a do akej vekovej skupiny patríte")
  print("Vyberte si",vstup1,"čo Vám môžem vypočítať \n1: Váš vek\n2: Koľko Vám zostáva do dôchodku\n3: Do akej vekovej kategorie patríte")
  vstup2=int(input("Zadajte vašu voľbu :"))
  print("\nVaša voľba je",vstup2)
  if vstup2==1:
    a=float(input("Zadajte Váš rok narodenia :"))
    b=float(input("Zadajte aktualný rok :"))
    print("Váš vek je",b-a,"rokov")
  elif vstup2==2:
    a=float(input("Váš aktualný vek "))
    b=float(65)
    print("Do dôchodku Vám zostáva",b-a,"rokov")
  elif vstup2==3:
    a=float(input("Zadajte svoj vek :"))
    if a<0 or a<18:
      print("Vy ste junior ")
    elif a<50:
      print("Ste v strednom veku ")
    elif a>50: 
      print("Vy ste senior ")
  time.sleep(1)