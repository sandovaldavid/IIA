#Encuentra la suma y la cantidad de los digitos de un numero entero

num = int(input("Enter a number: "))

def digitos(num):
    flag = True
    digit = 0
    newnum = num
    while flag:
        newnum = int(newnum/10)
        if newnum != 0:
            digit = digit + 1
        else:
            flag = False
    return digit+1

print(f"The digits of this number are: {digitos(num)}")

def suma(num):
    numDig = digitos(num)
    sum = 0
    i = 0
    while i < numDig:
        sum = sum + (num % 10)
        num = int(num/10)
        i = i + 1
    return sum

print(f"The sum of the digits of this number is: {suma(num)}")