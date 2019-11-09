def Sum(lis):
  sum = 0;
  for i in range(0, len(lis), 1):
    sum = sum + lis[i]
  return sum;

def main():
 size = int(input("Enter number of elements:"))
 list1 = list();

 for i in range(0,size,1):
    print("Enter element {}".format(i+1));
    list1.append(int(input()));

    res = Sum(list1)

 print("Addition of all the elements is:",res)

if(__name__ =="__main__"):
  main();
