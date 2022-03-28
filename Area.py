
def rectangle(a,b):
    return a*b

def perimeter_rect(a,b):
    return 2*   (a*b)

def area_square(a):
    return a*a


if __name__=="__main__":

    check = 1
    while check:
        c = int(input("main menu \n 1) Find Area of rectangle\n 2) Find perimeter of Rectangle \n 3) Find Area of Square\n 4) Exit"))

        if c==1:
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))
            result = rectangle(num1,num2)
            print(result)

        elif c==2:
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))
            result1 = perimeter_rect(num1,num2)
            print(result1)
        elif c==3:
            num1 = int(input("enter side of square: "))
            result2 = area_square(num1)
            print(result2)
        else:
            check = 0
            print("Exit")
