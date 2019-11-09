def main():
 size = int(input("Enter number of elements:"))
 list1 = list();

 for i in range(0,size,1):
    print("Enter element {}".format(i+1));
    list1.append(int(input()));

 no1 = int(input("Enter element to be search:"))
 res = frequency(list1,no1)

 print("Element occurs",res,"times")

def frequency(list,no):
    count = 0
    for i in range(0,len(list),1):
        if(list[i] == no):
            count = count+1
    return count

if(__name__ =="__main__"):
  main();
