klar = False
list = []
while klar == False:
    choice = input('Vad vill du göra? ' \
    '1. Lägg till på Att göra listan. ' \
    '2. Ta bort från listan. ' \
    '3. Visa hela listan. ' \
    '4. Avsluta ')
    if int(choice) == 1:
        list.append(input('Vad vill du lägga till?'))
    elif int(choice) == 2:
        list.remove(input('Vad vill du ta bort?'))
    elif int(choice) == 3:
        print(list)
    elif int(choice) == 4:
        klar = True
