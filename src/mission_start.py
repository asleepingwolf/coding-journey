from common.interface import clear_screen, show_header

def main():
    clear_screen()
    show_header("System Initialized")
    
    name = input("Ange ditt kodnamn: ")
    print(f"\nVälkommen, {name}. Fas 1 har börjat.")

if __name__ == "__main__":
    main()