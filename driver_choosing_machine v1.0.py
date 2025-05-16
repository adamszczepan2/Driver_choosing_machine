import random, time

condition = True

while condition:
    drivers = ['Adam', 'Bodek', 'Maciek', 'Oskar']
    print()
    print(f'Losowania zaszczytu wzięcia samochodu dostąpią: {drivers}\n')
    time.sleep(1)
    decision = input("Gotowy na wybór skazańca, ekhm... kierowcy? T/N: ")
    print()

    if decision.lower() == 't':
        print("Uwaga Achtung Wnimanje!\n")
        i = len(drivers)-1
        while i > 0:
            chosen = random.choices(drivers)
            drivers.remove(chosen[0])
            time.sleep(2.5)
            print(f'Samochodu nie weźmie {chosen[0]}...\n')
            i -= 1   
        print(f'Alleluja, klękajcie narody! Wybrańcem, jedynym Sprawiedliwym Wśród Narodów- zostaje {drivers[0]}!\n')
    elif decision.lower() == 'n':
        break
    else:
        print("Wprowadź literę 'T' aby kontynuować, lub 'N' aby zakończyć")
    
    continuation = input("Czy powtórzyć wybór? T/N: ")
    while continuation.lower() not in ('t', 'n'):
        continuation = input("Wprowadź literę 'T' aby kontynuować, lub 'N' aby zakończyć")

    if continuation.lower() == 'n':
        condition = not condition

print("-" * 33)
print("Miłego dzionka i smacznej kawusi!")
print("-" * 33)