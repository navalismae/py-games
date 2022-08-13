
dataBase = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

secondBase = []
for element in dataBase:
    secondBase.append(element**2)

thirdBase = [
            element
            for element in dataBase
            if element % 2 == 0
            ]

print(secondBase)
print(thirdBase)


numbers = (
            number
            for number in range(2, 471)
            if number % 7 == 0
            if number % 5 != 0

          )
for item in numbers:
    print(item)