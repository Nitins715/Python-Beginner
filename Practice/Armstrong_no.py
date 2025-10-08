def isArmstrong(num: int) -> bool:
    original = num 
    check = 0
    order = len(str(num))
    while(num>0):
        res = num%10
        num //= 10
        check += res ** order
    return check == original       

if __name__ == "__main__":
    num = int(input("Enter your number to check Armstrong number: "))
    if isArmstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")      

  
    # upper_limit = int(input("Enter range to find armstrong number: "))
    # for i in range(upper_limit):
    #     if isArmstrong(i):
    #         print(f"{i} is an Armstrong number")   
