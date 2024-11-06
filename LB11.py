def Linearsearch(arr , x):
    for i in range(len(arr)):
        if arr[i]  ==x:
            return i
        return  -1

def sentsearch(arr ,x):
    l = len(arr)
    arr.append(x)
    i=0
    while(arr[i]!=x):
        i = i+1
        if(i!=1):
            return i
        else :
            return -1

def Binsearch(arr, key):
    low= 0
    high = len(arr)-1
    m = 0
    while(low<=high):
        m = (low+high)//2
        if(key<arr[m]):
            high = m-1
        elif (key>arr[m]):
            low = m+1
        else :
            return m
    
    return -1

def Fibsearch(arr , key, n):
    b=0
    a=-1
    F = b+a
    while(F<n):
        b=a
        a=F
        F = b+a
    offset = -1
    
    while(F>1):
        i = min(offset + b , n-1)
        if(arr[i] < key):
            F = a
            a =b
            b = F-a
            offset = i
        elif(arr[i]>key):
            F =b
            a= a-b
            b = F-a
        else : 
            return i
    
    if(a and arr[offset +i]==key):
        return offset +1
    
    return -1

print("\nHow many students are there? " )
n = int(input())
array = []
i=0
for i in range(n):
    print("\nEnter roll number : ")
    item = int(input())
    array.append(item)

print("\nThe Roll numbers of students are : \n")
print(array)

key = int(input("\nEnter the roll number to be searched : "))
location1 = Binsearch(array , key )

if(location1!=-1):
    print("\nThe search is successful by binary search\n")
else : 
    print("\nThe element is not found")

key1 = int(input("\nEnter the roll number to be searched : "))
location2 = Linearsearch(array , key )
if(location2!=-1):
    print("\nThe search is successful by linear search")
else :
    print("\nThe element is not found")

key2 = int(input("\nEnter roll number to be searched : "))
location3 = sentsearch(array , key2)
if(location3!=-1):
    print("\nThe search is successful by sentinal search")
else : 
    print("\nThe element is not found")

key3 = int(input("\nEnter roll number to be searched : "))
location4 = Fibsearch(array , key3 ,n)
if(location4!=-1):
    print("\nThe search is successful by Fibonacci search")
else : 
    print("\nThe element is not found")