import time
def list_add(x,y):
  x.append(y)

def list_removing(y):
  zoznam.remove(y)
  
def list_adding_by_possition(zoznam,f,g):
  zoznam.insert(int(f),g)

def list_clearing(zoznam):
  zoznam.clear()


zoznam=[]

while True :
  print('\x1bc') 
  print("Vitajte :)\n Ak chete pokračovať stlačte A ak nie stlačte N")
  vstup=input()
  if vstup in "Aa":
    print("Program bude pokračovať \nSpracovávam....\n.....\n....")
  else:
    break
  print("Menu : \n1.Pridanie do zoznamu\n2.Pridanie do zoznamu na pozíciu z klavesnice\n3.Výmazavanie konkretného záznamu(slovný zápis)\n4.Vymazanie konkretného záznamu pomocou indexu\n5.Vyčistenie celého zoznamu\n6.Výpis zoznámu")
  vstup2=input()
  if vstup2=="1":
    x=input("Zadajte meno :")
    list_add(zoznam, x)
  elif vstup2=="2":
    g=input("Zadajte meno : ")
    f=int(input("Zadajte pozíciu :"))
    zoznam.insert(f, g)
    print(zoznam )
  elif vstup2=="3":
    g=input("Zadajte meno : ")
    list_removing(zoznam,g)
    print()
  elif vstup2=="4":
    e=int(input("Zadajte index :"))
    del zoznam[e]
    print(zoznam)
  elif vstup2=="5":
    list_clearing(zoznam)
    print(zoznam)
  elif vstup2=="6":
    print(zoznam)
  time.sleep(5)