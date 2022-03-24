import math
while True:
 
  
  print ("Vítajte v programe kalkulačka\nPonuka:\n1 sčítanie\n2 odčítanie\n3 násobenie\n4 delenie\n5 n-ta mocnina\n6 n-ta odmocnina\n7 kvadratická rovnica\n8 Pytagorová veta\n9 Objem a obsah kvádra")
  vstup=int(input("Zadajte svoju voľbu:"))
  print ("Vaša voľba je :",vstup)
  if vstup==1:
    a=float(input("Zadaj prvé číslo:"))
    b=float(input("Zadaj druhé číslo:"))
    print("Sčítanie čísel ",a,"+",b,"=",a+b)
  elif vstup==2:
    a=float(input("Zadaj prvé číslo:"))
    b=float(input("Zadaj druhé číslo:"))
    print("Odčítanie čísel ",a,"-",b,"=",a-b)
  elif vstup==3:
    a=float(input("Zadaj prvé číslo:"))
    b=float(input("Zadaj druhé číslo:"))
    print("Násobenie čísel",a,"*",b,"=",a*b)
  elif vstup==4:
    a=float(input("Zadaj prvé číslo:"))
    b=float(input("Zadaj druhé číslo:"))
    if a==0:
      print("Nulou sa nedá deliť")
    else :
      print("Delenie čísel ",a,"/",b,"=",a/b)
  elif vstup==5:
    a=float(input("Zadaj číslo :"))
    n=float(input("Zadaj mocninu:"))
    print(n,"-tá mocnicna čísla",a,"=",a**n)
  elif vstup==6:
    a=float(input("Zadaj číslo:"))
    n=float(input("Zadaj odmocninu:"))
    print(n,"-tá odmocnina čísla",a,"=",a**(1/n))
  elif vstup==0:
    print("Dovidenia !!!")
    exit()
  elif vstup==7:
    a=int(input("Zadaj hodnotu a :"))
    b=int(input("Zadaj hodnotu b :"))
    c=int(input("Zadaj hodnotu c :"))
    print("Hodnoty sú a=",a,"b=",b,"c=",c)
    D=b*b-4*a*c
    print("Diskrimants sa rovná=",D)
    if D<0 :
      print("Rovnica nemá riešenie v R")
    if D==0:
      x=(-b)/2*a
      print("x=",x)
    if D>0 :
      x1=((-b)+math.sqrt(D)/2*a)
      x2=((-b)-math.sqrt(D)/2*a)
      print("x1=",x1,"x2=",x2)
  elif vstup==8:
    a=float(input("Zadaj hodnotu a :"))
    b=float(input("Zadaj hodnotu b :"))
    c=math.sqrt((a**2)+(b**2))
    print("Strana c je ",c,"\n\n")
  elif vstup==9:
    print("1.Kváder\n2.Kocka")
    vstup2=int(input("Zadajte svoju voľbu "))
    if vstup2==1:
      a=float(input("Zadajte stranu a :"))
      b= float(input("Zadajte stranu b :"))
      c=float(input("Zadajte stranu c :"))
      V=a*b*c
      S=(2*a*b)+(2*b*c)+(2*a*c)
      print("Objem kvádra je V=",V,"a obsah kvádra je S=",S)
    if vstup2==2:
      a=float(input("Zadajte stranu a :"))
      if a==0:
        print("Kocka so stranou 0 neexistuje")
        exit()
      V=a*a*a
      S=6*a*a
      print("Objem kocky je V=",V,"a obsah kocky je S=",S)
      print('\x1bc')

