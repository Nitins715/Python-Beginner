def matrix(m,n):
    col = []
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"Enter val[{i}][{j}] : "))
            row.append(val)
        col.append(row)
    return col

def sum(A,B):
    col = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        col.append(row)
    return col

def mul(A, B):
    # Ensure multiplication dimensions are valid
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible: columns of A != rows of B")
        return []

    # Initialize C with zeros
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Multiply
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


if __name__ == "__main__":
    m = int(input("Enter no of rows for A: "))    
    n = int(input("Enter no of columns for A: "))    

    print("Enter matrix A:")
    A = matrix(m, n)

    p = int(input("Enter no of rows for B: "))    
    q = int(input("Enter no of columns for B: "))    

    print("Enter matrix B:")
    B = matrix(p, q)

    print("\nSum of matrices:")
    if m == p and n == q:
        for row in sum(A, B):
            print(*row)
    else:
        print("Matrix addition not possible: dimensions do not match")

    print("\nProduct of matrices:")
    for row in mul(A, B):
        print(*row)
