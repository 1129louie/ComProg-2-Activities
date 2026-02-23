x = 300

def find_closest():
    print("Find the closest number to 300")
    print()

    a = int(input("Enter your first number: "))
    print()
    b = int(input("Enter your second number: "))
    print()
    c = int(input("Enter your third number: "))
    print()

    if a == b == c:
        print(f"A is {a}, B is {b}, and C with the value of {c} are all equal, therefore all numbers are closest to {x}")
    else:
        diffA = abs(x - a)
        diffB = abs(x - b)
        diffC = abs(x - c)

        if diffA <= diffB and diffA <= diffC:
            print(f"A with the value of {a} is closest to {x}")
        elif diffB <= diffA and diffB <= diffC:
            print(f"B with the value of {b} is closest to {x}")
        else:
            print(f"C with the value of {c} is closest to {x}")

find_closest()