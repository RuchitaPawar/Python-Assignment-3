def Minimum(lis):
  min = lis[0]
  for i in range(0, len(lis), 1):
    if(lis[i] < min):
        min = lis[i]
  return min;

def main():
 size = int(input("Enter number of elements:"))
 list1 = list();

 for i in range(0,size,1):
    print("Enter element {}".format(i+1));
    list1.append(int(input()));

    res = Minimum(list1)

 print("Minimum number from list is:",res)

if(__name__ =="__main__"):
  main();

