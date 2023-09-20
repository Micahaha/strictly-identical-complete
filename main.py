from serialsearch import *



def compare_lists(l1, l2):

    SIZE1 = len(l1) -1
    SIZE2 = len(l2) -1  
    index = 0

    if(SIZE1 == SIZE2):
        for i in l1:
            if search(l2, index ,SIZE1, i) == -1:
                print("Not Identitical")
            else:
                print("Identitcal")
            index+=1
    else:
        return False

def main():
    list1 = ['A','C','C']
    list2 = ['A','B','C']
    
    print(compare_lists(list1,list2))


main()


