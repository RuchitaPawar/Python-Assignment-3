def Maximum(lis):
  max = 0;
  for i in range(0, len(lis), 1):
    if(lis[i] > max):
        max = lis[i]
  return max;

def main():
 size = int(input("Enter number of elements:"))
 list1 = list();

 for i in range(0,size,1):
    print("Enter element {}".format(i+1));
    list1.append(int(input()));

    res = Maximum(list1)

 print("Maximum number from list is:",res)

if(__name__ =="__main__"):
  main();
