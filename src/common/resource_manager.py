import json
import os

def load_monsters():
    # Vi måste hitta rätt söksteg till data-mappen
    # Denna rad letar upp mappen som src ligger i, och går sedan till data/
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, 'data', 'monsters.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Fel: Kunde inte hitta {file_path}")
        return []

# Testa funktionen
if __name__ == "__main__":
    monsters = load_monsters()
    for m in monsters:
        print(f"Hittade monster: {m['name']} med {m['health']} HP")