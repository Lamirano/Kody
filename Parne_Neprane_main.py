#Prográm na zistenie parného alebo neparného číšla. 
def strange_reverse(seq, condition):
  mainlist=[]
  if condition == "odd":
    seq = seq[::-1]
    for number in seq:
      if not(number in range(0,(99*1000000),2)):
        if number >= 0:
          mainlist.append(number)
  elif condition == "even":
    seq = seq[::-1]
    for number in seq:
      if (number in range(0,(99*1000000),2)):
        if number >= 0:
          mainlist.append(number)
  return mainlist



def main():
 test_seq = [-5, 4, 7, 8, 9]
 result = strange_reverse(test_seq, "odd") 
 result2 = strange_reverse(test_seq, "even")
 print(result)
 print(result2)
main()
  
