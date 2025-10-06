def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1) 
    # fr = 1
    # for i in range(1,num+1):
    #     fr *= i
    # return fr  

def trailingzero(num):
    count = 0 
    i = 5
    while(num//i != 0):
        count += int(num/i)
        i = i*5
    return count    

def main():
    while True: 
        num = input("Enter number to find factorial (or 'q' to quit): ").strip()
        if num.lower() == "q":
            break       
        try:
            num = int(num)
        except ValueError:
            print("Invalid input. Please enter a whole number or 'q'.")
            continue 
        if num < 0:
            print("Please enter a non-negative integer.")
            continue
        if num < 20:
            res = fact(num)
            print(f"Factorial of {num} is {res}")
        else:
            res = trailingzero(num)
            print(f"The factorial of {num} contains {res} trailing zero.")
               
if __name__ == "__main__":
    main()           
