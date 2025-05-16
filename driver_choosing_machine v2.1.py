"""
Autor: Adam Szczepaniak

Data: 09.05.2025

Wersja: 2.1

Opis programu: 
Program powstał jako odpowiedź na "problem" braku chętnych do wzięcia samochodu i jego prowadzenia podczas wspólnego wyjazdu ze znajomymi. 
Przeprowadza losowanie jednego z wprowadzonych uczestników wyjazdu. Zakłada się, że zwycięzca losowania bierze swój samochód i zostaje kierowcą 
na czas wyjazdu. Autor nie ponosi odpowiedzialności za brak chęci wzięcia samochodu przez zwycięzcę mimo poprawnie przeprowadzonej procedury 
losowania.

Opis działania programu: 
Program wyświetla menu główne, z którego można wybrać opcje- wyświetlenie, dodanie, usunięcie, zmianę kolejności, losowanie kierowców,
lub wyjście z programu. 
Opcja 1 wyświetla obecnych kierowców- zwraca stan bazy kierowców na daną chwilę. Po uruchomieniu programu jest ona pusta. 
Dodanie kierowców umożliwia opcja 2. Poszczególne imiona należy wpisać rozdzielając je spacją. Opcji można używać wielokrotnie. W przypadku 
ponownego dodania imion do już utworzonej bazy program sprawdza, czy dane imię znajduje się już w bazie i w takim przypadku go nie dodaje.
Wybranie opcji 3 powoduje przejście do menu usuwania kierowców. Istnieje możliwość usunięcia wskazanych, wpisanych przez użytkownika imion
kierowców, lub usunięcie wszystkich kierowców z bazy. W pierwszym przypadku należy wyjść z menu usuwania kierowców do menu głównego, 
natomiast w drugim program robi to automatycznie.
Opcja 4 zmienia kolejność imion w bazie kierowców. Powstała, aby pozwolić użytkownikowi na zachowanie jak największej losowości wyboru. 
Opcji można używać wielokrotnie przed właściwym losowaniem. 
Opcja 5 rozpoczyna procedurę losowania metodą eliminacji. Program losowo wskazuje kolejne imiona osób, które nie zostaną kierowcami. Osoba, 
której imię jako jedyne pozostanie w bazie wygrywa losowanie.
Opcja 6 pozwala na zakończenie działania programu.
"""
import random, time

def intro():
    # Funkcja wyświetlająca intro programu
    message = f"\n{'-'*121}\n|{' '*119}|\n|{'Kiedy nikt nie chce prowadzić- ten program \
wylosuje kierowcę!': ^119}|\n|{' '*119}|\n{'-'*121}\n"
    print(message)
    time.sleep(1)

def menu():
    # Funkcja wyswietlająca menu główne programu oraz zwracająca wybór użytkownika do modułu głównego
    menu = f"{'Menu:':-^121}\n\n1. Naciśnij 1 aby wyświetlić obecnych kierowców.\n\n\
2. Naciśnij 2 aby dodać kierowców.\n\n3. Naciśnij 3 aby usunąć kierowców.\n\n\
4. Naciśnij 4 aby zmienić kolejność kierowców.\n\n5. Naciśnij 5 aby wylosować kierowcę.\n\n\
6. Naciśnij 0 aby zakończyć działanie programu.\n\n{'-'*121}\n"  
    print(menu)
    choice = input("Dokonaj wyboru: ")
    print()
    while choice not in ('0','1', '2', '3', '4', '5'):
        choice = input(f"Wybierz od 1 do 5 lub 0- aby wyjść z programu. ")
        print()
    return int(choice)

def current_drivers(drivers):
    # Funkcja wyświetlająca zawartość listy kierowców i ustawiająca jej wartość w module głównym
    if len(drivers) == 0:
        print(f"W bazie kierowców nie ma żadnych rekordów.\n")
    else:
        print(f'Obecni kierowcy to: {", ".join(driver for driver in drivers)}.\n')
    time.sleep(1)
    globals()['drivers'] = drivers

def drivers_input():
    # Funkcja pomocnicza, wprowadza a następnie przeprowadza walidację wprowadzonych rekordów
    input_drivers, to_delete = [], []
    input_drivers = input("Wprowadź imiona rozdzielone spacją: ").title().split(" ") 
    print()
    for input_driver in input_drivers:
        input_driver.strip()
        if len(input_driver) == 0:
            to_delete.append(input_driver)
    for driver_to_del in to_delete:
        if driver_to_del in input_drivers:
            input_drivers.remove(driver_to_del)
    return input_drivers

def add_new_drivers(drivers):
    # Funkcja dodająca nowych kierowców do bazy.
    new_drivers = drivers_input() 
    for driver in drivers:
        if driver in new_drivers:
            print(f"{driver} znajduje się już w bazie kierowców.\n")
            time.sleep(1)
            new_drivers.remove(driver)  
    for new_driver in new_drivers:    
        drivers.append(new_driver)
    if len(new_drivers) == 0:
        print("Do bazy kierowców nie dodano nowych rekordów.\n")
    else:
        print(f'Dodano następujących kierowców: {", ".join(new_driver for new_driver in new_drivers)}.\n')
    time.sleep(1)
    current_drivers(drivers)

def del_menu():
    # Funkcja wyswietlająca menu usuwania kierowców oraz zwracająca wybór użytkownika
    del_menu = f"{'Menu usuwania kierowców:':-^121}\n\n1. Naciśnij 1 aby wyświetlić obecnych kierowców.\n\n\
2. Naciśnij 2 aby usunąć wskazanych kierowców.\n\n3. Naciśnij 3 aby usunąć wszystkich kierowców z bazy.\n\n\
4. Naciśnij 0 aby wyjść do Menu gównego.\n\n{'-'*121}\n"
    print(del_menu)
    choice = input("Dokonaj wyboru: ")
    print()
    while choice not in ('0','1', '2', '3'):
        choice = input(f"Wybierz od 1, 2, 3 lub 0- wyjść do menu głównego. ")
        print()
    return(int(choice))

def delete_drivers(drivers):
    # Funkcja wyswietlająca menu i usuwająca kierowców z bazy oraz zwracająca efekt działań do bazy kierowców
    del_choice = del_menu()
    while del_choice:
        match del_choice:
            case 0:
                globals()['menu_choice'] = menu()
            case 1:
                current_drivers(drivers)
                del_choice = del_menu()               
            case 2:
                del_drivers = drivers_input()
                print() 
                for del_driver in del_drivers:
                    if del_driver in drivers:
                        drivers.remove(del_driver)
                    else:
                        print(f"Nie znaleziono kierowcy {del_driver} w bazie kierowców.\n")
                        time.sleep(1)
                        del_drivers.remove(del_driver)
                if len(del_drivers) != 0:
                    print(f'Usunięto kierowców: {", ".join(del_driver for del_driver in del_drivers)}.\n')
                    time.sleep(1)
                current_drivers(drivers)
                del_choice = del_menu()
            case 3:
                print(f"Usuwam dane wszystkich kierowców...\n")
                time.sleep(1)
                drivers = []
                current_drivers(drivers)
                print(f"Automatyczne wyjście z Menu usuwania kierowców do Menu głównego...\n")
                time.sleep(1)
                del_choice = 0
    
def shuffle_drivers(drivers):
    # Funkcja zmieniająca kolejność wyświetlania kierowców w bazie
    print('Zmieniam kolejność kierowców...\n')
    time.sleep(1)
    random.shuffle(drivers)
    current_drivers(drivers)

def choose_driver(drivers):
    # Funkcja wybierająca zwycięzcę losowania
    current_drivers(drivers)
    choose_drivers = drivers.copy()
    i = len(choose_drivers) - 1
    print('Rozpoczynamy losowanie...\n')
    time.sleep(1)
    while i > 0:
        chosen = random.choices(choose_drivers)
        choose_drivers.remove(chosen[0])
        time.sleep(1)
        print(f'Kierowcą nie będzie {chosen[0]}...\n')
        i -= 1  
    time.sleep(1)
    print(f'Zwycięzcą losowania zostaje {choose_drivers[0]}!\n')
    time.sleep(2)

# dodać usuwanie znaków specjalnych z imion
# dodać sprawdzenie, czy imiona są wprowadzone kilkukrotnie i jeśli tak, usunięcie duplikatów
# dodać ograniczenie długości imion do 15 znaków

intro()    
drivers = []
while True:
    menu_choice = menu() 
    match menu_choice:
        case 0: 
            print(f"{'Miłego dzionka i smacznej kawusi!':-^121}\n")
            quit()
        case 1:
            current_drivers(drivers)
        case 2:
            add_new_drivers(drivers)
        case 3:
            delete_drivers(drivers)
        case 4:
            shuffle_drivers(drivers)
        case 5:
            choose_driver(drivers)



