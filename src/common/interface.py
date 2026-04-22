
def clear_screen():
    """Rensar terminalen så att det ser snyggt ut."""
    import os
    # Rensar beroende på om du kör Windows (cls) eller Mac/Linux (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title):
    """Skriver ut en snygg rubrik."""
    print("=" * 30)
    print(f"--- {title.upper()} ---")
    print("=" * 30)