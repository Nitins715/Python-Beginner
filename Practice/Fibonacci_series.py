import time 

#Recursive approach
def fibRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2,n+1):
        return fibRec(n-1)+fibRec(n-2)

def fibIte(n):
    a = 0
    b = 1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(1,n):
        temp = b
        b = a+b
        a = temp
        print(b , end=" ")
    return True    

if __name__ == "__main__":
    n = int(input("Enter your number : "))
    init = time.time()
    # res = fibRec(n)
    # print(res)
    fibIte(n)        
    print(f"It took {time.time() - init} seconds")
