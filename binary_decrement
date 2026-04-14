# assigning a numerical value to each card (face-down = 1, face-up = 0) and showing that each move strictly decreases the value of the overall binary number, meaning it must eventually reach zero

def move(a):
    for i in range(len(a)):
        if a[i] == '1':
            a[i] = '0'
            if i + 1 < len(a):
                a[i+1] = '1' if a[i+1] == '0' else '0'
            break
    return a

if __name__ == "__main__":
    a = list(input("Enter your cards positions (0,1): "))
    print(" ".join(a))
    while any(bit == '1' for bit in a):
        a = move(a.copy())
        print(a)
    print(" ".join(a))
