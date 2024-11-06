def insert(result) : 
    result = []
    a = int(input("Enter the rows of matrix 1 : "))
    b = int(input("Enter columns of matrix 2 : "))
    for i in range(a): 
        temp = []
        for j in range(b): 
            c = int(input("Enter element : "))
            temp.append(c)
        result.append(temp)
        
    return result

def addition(X ,Y , size1 ,size2): 
    if(size1!=size2): 
        print("Addition of the matrix is not possible")
    else: 
        result = []
        for i in range(size1): 
            temp = []
            for j in range(size2): 
                temp.append(0)
            result.append(temp)
                
        # iterate through rows
        for i in range(len(X)):
            # iterate through columns
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]

        for r in result:
            print(r)
        
def subtraction(matrix1, matrix2 , size1 ,size2): 
    if(size1!=size2): 
        print("Addition of the matrix is not possible")
    else: 
        rmatrix = []
        for i in range(size1): 
            temp = []
            for j in range(size2): 
                temp.append(0)
            rmatrix.append(temp)
            
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]

        for r in rmatrix:
            print(r)

def display(X): 
    for i in X: 
        for j in i :
            print(j , end=" ")
        print()

def multiplication(A , B , size1 , size2): 
    result = []
    for i in range(size1): 
        temp = []
        for j in range(size2): 
            temp.append(0)
        result.append(temp)            

    # iterating by row of A
    for i in range(len(A)):
    
        # iterating by column by B
        for j in range(len(B[0])):
    
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    for r in result:
        print(r)

def transpose(X , size1): 
    result = []
    for i in range(size1): 
        temp = []
        for j in range(size1):
            temp.append(0)
        result.append(temp)
            
    # iterate through rows
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    for r in result:
        print(r)

def main(): 
    X  = []
    Y = []
    print("Insert elements in 1st matrix : ")
    X = insert(X)
    print("Insert elements in 2nd matrix : ")
    Y = insert(Y)

    size1 = len(X)
    print("size1 : " , size1)
    size2=0
    flag =0
    for i in Y:
        for j in i: 
            size2 = size2 +1
            flag=1
        if(flag==1): 
            break
        
    print("size2 : " , size2)
    
    print("\nDisplaying matrix 1 : ")
    display(X)
    print("\nDisplaying matrix 2 : ")
    display(Y)
    print("Addition of 2 matrices : ")
    addition(X , Y , size1 ,size2)
    print("\nSubtraction of 2 matrices : ")
    subtraction(X , Y , size1, size2)
    print("Multiplication of 2 matrices : ")
    multiplication(X , Y , size1, size2)
    print("")
    print("Transpose of 1st Matrix : ")
    transpose(X , size1)
    print("Transpose of 2nd Matrix  :")
    transpose(Y ,size2)


main()

