lst1=[]
lst2=[]
def find(L1,L2):
    for elem in L1:
        for elem1 in L2:
            if elem==elem1:
                lst1.append(elem)
                break
        else:
            lst2.append(elem)
    print(lst1)
    print(lst2)

L1=list(input("enter 1st list"))
# L1=[int(i) for i in L1]
L2=list(input("enter 2nd list"))
# L1=[int(j) for j in L2]
find(L1,L2)


