import random

print ("Hej. Zgadnij liczbe z zakresu od 1 do 10. Masz 5 prób!: ")
randomNumber = random.randint(1, 10)
for i in range(5):
    print(randomNumber)
    podanaliczba = input("Podaj liczbe, to Twoja " + str(i+1) + " próba:")
    if int(podanaliczba) > randomNumber:
        print("Podana liczba jest za duza!")
    elif int(podanaliczba) < randomNumber:
        print("Podana liczba jest za mala!")
    else:
        print("Podano prawidłową liczbę!")
        break

print("Nie udało Ci się odgadnąć liczby! :c")

