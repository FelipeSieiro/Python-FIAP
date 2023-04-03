num1 = int(input("1º número: "))
num2 = int(input("2º número: "))
num3 = int(input("3º número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
else:
    if num1 >= num2:
        print(num2, num1, num3)
    else:
        print(num1, num2, num3)
