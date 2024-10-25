year = input("Enter a year: ")

if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    print(year + " is a leap year.")
else:
    print(year + " is not a leap year.")

# Usando expresión lambda
answer = lambda x: x % 4 == 0 and x % 100 != 0 or x % 400 == 0
