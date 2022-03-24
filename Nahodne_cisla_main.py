#Využitie importu randint na pád nahodneho čisla. 
from random import randint
u=0
g=int(input("Zadajte počet hodov : "))
pocty = [0]*6
for i in range(g):
  hod =randint(1, 6)
  u=u+1
  print(u,"Hod")
  pocet = pocty[hod-1]+1
  print('Už {}-krát padlo číslo {}.'.format(pocet, hod))
  pocty[hod-1] += 1

for i in range(6):
  print('Číslo {} padlo {}-krát.'.format(i+1, pocty[i]))
