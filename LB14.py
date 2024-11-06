# Selection Sort algorithm
# Bubble sort algorithm

def selection_sort(l): 
    for i in range(len(l))  :
        temp =0
        for j in range(i+1,len(l)): 
            if(l[j]<l[i]) :
                temp =l[i]
                l[i] = l[j]
                l[j] = temp    
    print("Selection sort result : ")
    print(l)
# O(N^2)

def bubble_sort(l) : 
    for k in range(0,len(l)) :
        for i in range(1,len(l)):
            if(l[i]<l[i-1]): 
                temp =l[i]
                l[i] = l[i-1]
                l[i-1] = temp
    print("\nBubble sort result : ")
    print(l)
    print("Top 5 numbers: ")
    display(l , len(l)-1)
# O(N^2)

def display(l, size):
    if((size+1)>=5): 
        count=0
        while(count!=5): 
            print(l[size])
            size = size-1
            count = count +1
    else: 
        print("Size is less than 5 ")

def main():
    n = int(input("Enter number of elements in the list : "))
    l = []
    for i in range(n): 
        a = int(input("Enter marks : "))
        l.append(a)
    selection_sort(l)
    bubble_sort(l)


main()