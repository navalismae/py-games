import os
import random
from enum import Enum



"""
1.Program dodaje elementy do bazy danych
2.Odczytuje zawartość po wykonaniu polecenia
3.Usuwa bezpośrednie rekordy 
4. Szuka rekordów

"""
dBase = [
        {'010101':{'imie': 'Stefan',    'nazwisko': 'Kowalski'}},
        {'020202':{'imie': 'Kamil', 'nazwisko': 'Tomaszewski'}},
        {'030303':{'imie': 'Asia', 'nazwisko': 'Tumialis'}},
        {'040404':{'imie': 'Michał', 'nazwisko': 'Rolkowski'}},
        ]

def showDataBase():
    for record in dBase:
        for key in record:
            print("ID: " , key, "| Imie i nazwisko: ", record[key]['imie'], record[key]['nazwisko'])

def menu():
    while True:
       
        choice = input("""
        Podaj zadanie, które chcesz wykonać:
        1. Pokaz baze danych
        2. Dodaj klienta
        3. Usuń klienta
        4. Znajdz klienta
        5. Wyjdź.
        """)
        if choice == '5':
            print("Dziekujemy za skorzystanie z programu.")
            break
        elif choice == '1':
            showDataBase()
        elif choice == '2':
            newRecord()
        elif choice == '3':
            delRecord()
        elif choice == '4':
            findRecord()
        else:
            print("Podaj poprawna instrukcje:")

def newRecord():
    name = input("Podaj imie uzytkownika: ")
    surname = input("Podaj nazwisko uzytkownika: ")
    userID = random.randint(100000, 999999)
    newDictionary = {str(userID):{'imie': name, 'nazwisko': surname}}
    dBase.append(newDictionary)
    
def delRecord():
    showDataBase()
    number = input("Ktory rekord chcesz usunąć? Podaj numer: ")
    for record in dBase:
        for key in record:
            if number in key:
                dBase.remove(record)
                break  
            else:
                print("Nie mamy takiego numeru")
                print(number)
        
def findRecord():
    number = input("Sprawdz czy rekord wystepuje w bazie danych!: ")
    recordInDataBase = False
    for record in dBase:
        for key in record:
            if number in key:
                recordInDataBase = True
                break

    if recordInDataBase:
        print("Rekord: ", number, " istnieje w bazie danych!")
    else:
        print("Nie ma takiego rekordu w bazie danych!")

while True:
    os.system('clear')
    menu()
    break