def insert(result ,size):
    print("Insert marks : ")
    for i in range(size): 
        marks = int(input("Enter marks : "))
        result.append(marks)
    return result

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
def display(result):
    for i in result: 
        print(i, end=" ")
        
    


def main(): 
    size = int(input("Enter number of student : "))
    result = []
    result = insert(result ,size)
    print("Sorting using quick sort")
    quickSort(result , 0 , size-1)
    print("Printing sorted array : ")
    display(result)
    print()

main()