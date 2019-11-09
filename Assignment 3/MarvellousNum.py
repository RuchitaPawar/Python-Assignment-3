def ChkPrime(no):
  for x in range(2,no,1):
    if ((no % x) == 0):
      return False
