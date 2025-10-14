# def lcm_iterative(a, b):
#     if a == 0 or b == 0:
#         return 0
#     a, b = abs(a), abs(b) 
#     max_num = max(a, b)     
#     while max_num % a != 0 or max_num % b != 0:
#         max_num += 1        
#     return max_num  

# def hcf_iterative(a,b):
#     if a>b:
#         mn = b
#     else:
#         mn = a    
#     for i in range(1,mn+1):
#         if a%i == 0 and b%i == 0:
#             hcf = i
#     return hcf 
                 
def hcf(a, b):
    """Euclidean algorithm"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """LCM(a,b) = (a*b)//HCF(a,b)"""
    if a == 0 or b == 0:
        return 0
    factor = hcf(a, b)
    return abs(a * b) // factor

if __name__ == "__main__":
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 1st number : "))

    print(f"LCM of {a} and {b} is {lcm(a,b)}")
    print(f"HCF of {a} and {b} is {hcf(a,b)}")
