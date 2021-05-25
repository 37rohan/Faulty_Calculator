#Exercise2

print("Welcome To Python Calculator")

while True:
    print("Choose operation * + - / ")
    operator = ["*","+","-","/"]
    operator = str(input())
    print("Give first value:")
    val1 = int(input())
    print("Give second value:")
    val2 = int(input())

    if val1 == 45 and val2 == 3 and operator == "*":
        print("Result: 555")
    elif val1 == 59 and val2 == 9 and operator == "+":
        print("Result: 77")
    elif val1 == 56 and val2 == 6 and operator == "/":
        print("Result: 4")
    elif operator == "*":
        print("Result:",val1 * val2)
    elif operator == "+":
        print("Result:",val1 + val2)
    elif operator == "-":
        print("Result:",val1 - val2)
    elif operator == "/":
        print("Result:",val1 / val2)
    elif operator == "**":
        print("Result:",val1 ** val2)
    else:
        print("You entered Wrong operator")
    repeat = input("If you want to do calculation again click y else n")
    if repeat == "y":
        continue
    else:
        print("Thanks for using this Calculator")


