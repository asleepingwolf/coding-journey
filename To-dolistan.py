klar = False
todo_list = [] # Ändrade namnet från 'list'

while not klar: # Snyggare sätt att skriva 'klar == False'
    # Lade till \n för att göra menyn mycket tydligare i terminalen
    choice = input('Vad vill du göra?\n' \
                   '1. Lägg till på Att göra listan.\n' \
                   '2. Ta bort från listan.\n' \
                   '3. Visa hela listan.\n' \
                   '4. Avsluta\n' \
                   'Ditt val: ')
                   
    if int(choice) == 1:
        todo_list.append(input('Vad vill du lägga till? '))
    elif int(choice) == 2:
        todo_list.remove(input('Vad vill du ta bort? '))
    elif int(choice) == 3:
        print(f"Här är din lista: {todo_list}")
    elif int(choice) == 4:
        klar = True
        print("Hej då!")