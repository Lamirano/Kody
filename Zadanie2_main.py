import time

while True:
  print('\x1bc')
  print("Vítajte v programe \n Ak si prajete pokračovať stlačte D ak nie tak C :")
  vstup=str(input())
  if vstup in "Dd":
    print("Spracovavam...\nSpracovavam...\nSpracovavam...") 
    retazec =str(input("\nUpozornenie veta musí obsahovať minimálne 20 znakov \nZadajte vetu :"))
    if len(retazec)<=20:
      retazec=(input("\nUpozornenie zadali ste vetu ktora obsahovala menej ako 20 znakov. \nZadajte prosím novu vetu :"))
      if len(retazec)<=20:
        print("Vaša veta ma menej ako 20 znakov, program sa vypne.")
        break
      else:
        print("Spracovavam...\nSpracovavam...\nSpracovavam...")
        print("Program bude pokračovať")
        nahradene_pismena=retazec.replace("a","w").replace("A","W").replace("o","x").replace("O","X")
        print("Zadana veta : ",retazec)
        print("Spracovavam...\nSpracovavam...\nSpracovavam...")
        print("Veta s nahradenými písmenami je :" ,nahradene_pismena)
    else:
        nahradene_pismena=retazec.replace("a","w").replace("A","W").replace("o","x").replace("O","X")
        print("Zadana veta : ",retazec)
        print("Spracovavam...\nSpracovavam...\nSpracovavam...")
        print("Veta s nahradenými písmenami je :" ,nahradene_pismena)
  else:
    print("Program sa vypne")
    break
  time.sleep(10)