def insert(arr):
    choice = 'y'
    while(choice=='y'): 
        name = input("Enter name to add : ")
        number = int(input("Enter number to add : "))
        temp = []
        temp.append(name )
        temp.append(number)
        arr.append(temp)
        choice = input("Do you want to enter more numbers ? (y/n) : ")
    return arr

def display(arr , n): 
    print("Phonebook list : \n")
    print("Name\t\tPhone Number")
    for i in range(n): 
        print(arr[i][0],end="\t\t")
        print(arr[i][1])
        
    print()

def input2(l): 
    n = int(input("Enter number of elements in the list : "))
    for i in range(n) : 
        temp = []
        name = input("Enter name : ")
        number = int(input("Enter number : "))
        temp.append(name)
        temp.append(number)
        l.append(temp)
        
    return l

def check(result): 
    if result!=-1:
        print("Name found at position : {0} " .format(result))
    else : 
        print("Name not found ")

def binarySearch_string_iterative(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high: 
        mid = (high + low)// 2
 
        if arr[mid][0] < x:
            low = mid + 1

        elif arr[mid][0] >x:
            high = mid -1

        else:
            return mid
    return -1

def binarySearch_string_recursive(arr,low ,high , x): 
    if high >= low:
        mid =(high+low)//2
        if arr[mid][0]==x:
            return mid
        elif arr[mid][0]>x:
            return binarySearch_string_recursive(arr, low, mid - 1, x)
 
        else:
            return binarySearch_string_recursive(arr, mid + 1, high, x)
    else:
        print("returning -1")
        return -1

def fibonacci_search(lst, target):
    size = len(lst)
    
    start = -1
    
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    
    
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < str(target):
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index][0] > str(target):
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1][0] == target):
        return size - 1
    return None

def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)
        
def FibonacciSearch(arr, x):
    m = 0 
    while FibonacciGenerator(m) < len(arr): 
        m = m + 1 
    offset = -1    
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        if (x > arr[i][0]):
            m = m - 1
            offset = i
        elif (x < arr[i][0]):
            m = m - 2
        else:
            return i        
    if(FibonacciGenerator(m - 1) and arr[offset + 1][0] == x):
        return offset + 1
    return -1



def main(): 
    l = []
    choice = 1
    n=0
    while(choice!=5): 
        print("------- MENU --------")
        print("1. Binary search iterative")
        print("2. Binary search recursive")
        print("3. Fibonacci Search")
        print("4. Insert and element in the phonebook")
        print("5. Display phonebook")
        print("6. Clear the phone")
        print("7. QUIT")
        choice = int(input("Enter choice : "))
        if(choice==1): 
            l = input2(l)
            target = input("Enter name to search : ")
            l.sort()
            result = binarySearch_string_iterative(l, target)
            check(result)
        elif(choice==2): 
            l = input2(l)
            target = input("Enter name to search : ")
            l.sort()
            n = len(l)
            result = binarySearch_string_recursive(l ,0, n-1,target)
            check(result)
        elif(choice==3): 
            l = input2(l)
            target = input("Enter name to search : ")
            result = FibonacciSearch(l , target)
            check(result)
        elif(choice==4): 
            l =insert(l)
            n = len(l)
        elif(choice==5): 
            display(l,n)
        elif(choice==6): 
            l.clear()
        elif(choice==7): 
            print("QUIT")
        else: print("Wrong choice")
        

main()