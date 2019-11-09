from MarvellousNum import *;

def main():
 size = int(input("Enter number of elements:"))
 list1 = list();
 primeList = list();

 for i in range(0,size,1):
    print("Enter element {}".format(i+1));
    list1.append(int(input()));

 for y in range(0,len(list1),1):
      res = ChkPrime(list1[y])
      if(not(res == False) ):
           primeList.append(list1[y])
 # print(primeList)
 total = ListPrime(primeList)
 print("Total of all the prime number from the list is :",total)

def ListPrime(primeList):
    sum = 0
    for x in range(0, len(primeList), 1):
     sum = sum + primeList[x]
    return sum

if(__name__ =="__main__"):
  main();