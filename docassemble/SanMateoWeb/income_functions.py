def Sort_Tuple(tup):
  lst = len(tup)
  for i in range(0, lst):
    for j in range(0, lst-i-1):
      if (tup[j][1] < tup[j + 1][1]):
        temp = tup[j]
        tup[j]= tup[j + 1]
        tup[j + 1]= temp
  return tup

def Tuple_Total(tup):
  tupletotal = 0
  lst = len(tup)
  for i in range(0, lst):
    tupletotal = tupletotal + tup[i][1]
  return tupletotal