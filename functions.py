def new_pos(x,n,malphabet):
  
  if x + n <= malphabet:
    return x + n
  else:
    a = x + n
    b = a - malphabet
    return b

