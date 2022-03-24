import math 
import time 
def adding(): 
  x=a+b
  return x

def subtracting():
  f=a-b
  return f

def multiplying():
  g=a*b
  return g

def dividing():
  p=a/b
  return p
  

def squaring():
  m=a**n
  return m

def root():
  w=a**(1/n)
  return w 

def quadratic_equation():
  D=b*b-4*a*c
  if D<0 :
    print("Rovnica nemá riešenie v R")
  if D==0:
    x=(-b)/2*a
    return x
  if D>0 :
    x1=((-b)+math.sqrt(D)/2*a)
    x2=((-b)-math.sqrt(D)/2*a)
    print("x1=",x1,"x2=",x2)

def pythagorean_theorem():
  c=math.sqrt((a**2)+(b**2))
  return c

def block_volume():
  V=a*b*c
  return V

def block_size():
  S=(2*a*b)+(2*b*c)+(2*a*c)
  return S 

def cube_volume():  
  V=a*a*a
  return V

def cube_size():
  S=6*a*a
  return S 

while True:
  print('\x1bc')
  print ("Vítajte v programe kalkulačka\nPonuka:\n0.Pre vypnutie kalkulačky\n1.Sčítanie\n2.Odčítanie\n3.Násobenie\n4.Delenie\n5.N-ta mocnina\n6.N-ta odmocnina\n7.Kvadratická rovnica\n8.Pytagorová veta\n9.Objem a obsah kvádra")
  vstup=int(input("Zadajte svoju voľbu:"))
  print ("\nVaša voľba je :",vstup)
  if vstup==1:
    a=float(input("Zadajte prvé číslo :"))
    b= float(input("Zadajte zadajte druhé číslo :"))
    print("Výsledok sčítania je :",adding())
  
  elif vstup==2:
    a=float(input("Zadajte prvé číslo:"))
    b=float(input("Zadajte druhé číslo:"))
    print("Výsledok odčítania je :",subtracting())

  elif vstup==3:
    a=float(input("Zadajte prvé číslo:"))
    b=float(input("Zadajte druhé číslo:"))
    print("Výsledok násobenia je :",multiplying())

  elif vstup==4:
    a=float(input("Zadajte prvé číslo:"))
    b=float(input("Zadajte druhé číslo:"))
    if a==0:
      print("Nulou sa nedá deliť")
    else :
      print("Výsledok delenia je :",dividing())
   
  elif vstup==5:
    a=float(input("Zadajte číslo :"))
    n=float(input("Zadajte mocninu :"))
    print("Výsledok n-tej mocniny je :",squaring())

  elif vstup==0:
    print("Dovidenia!")
    break

  elif vstup==6:
    a=float(input("Zadajte číslo :"))
    n=float(input("Zadajte odmocninu :"))
    print("Výsledok n-tej odmocniny je :",root())
  
  elif vstup==7:
    a=int(input("Zadajte hodnotu a :"))
    b=int(input("Zadajte hodnotu b :"))
    c=int(input("Zadajte hodnotu c :"))
    print("Hodnoty sú a=",a,"b=",b,"c=",c)
    print("Výsledok kvadratickej rovnice je :",quadratic_equation())

  elif vstup==8:
    a=float(input("Zadajte hodnotu a :"))
    b=float(input("Zadajte hodnotu b :"))
    print("Výsledok pythagorovej vety je c=",pythagorean_theorem())
  
  elif vstup==9:
    print("1.Kváder\n2.Kocka")
    vstup2=int(input("Zadajte svoju voľbu "))
    if vstup2==1:
      a=float(input("Zadajte stranu a :"))
      b= float(input("Zadajte stranu b :"))
      c=float(input("Zadajte stranu c :"))
      print("Objem kvádra je :",block_volume())
      print("Obsah kvádra je :",block_size())
    if vstup2==2:
      a=float(input("Zadajte stranu a :"))
      if a==0:
        print("Kocka so stranou 0 neexistuje")
        exit()
      print("Objem kocky je :",cube_volume())
      print("Obsah kocky je :",cube_size())
  time.sleep(7)  