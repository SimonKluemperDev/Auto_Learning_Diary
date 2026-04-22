import os
import json
from datetime import datetime

# Konfiguration
BASE_DIR = r"C:\Users\Workstation\Learning"
LOG_FILE = os.path.join(BASE_DIR, "DIARY.md")
DATA_FILE = os.path.join(BASE_DIR, ".data.json")

def get_input():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    print("--- Neuer Eintrag ---")
    category = input("Kategorie: ").strip()
    title = input("Titel: ").strip()
    description = input("Beschreibung: ").strip()
    reason = input("Warum/Problem: ").strip()
    date_str = datetime.now().strftime("%d.%m.%Y")
    return date_str, category, title, description, reason

def load_entries():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError: return []
    return []

def save_all(entries):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4)
    
    # Sortierung: Datum absteigend, Kategorie alphabetisch
    entries.sort(key=lambda x: (datetime.strptime(x['date'], "%d.%m.%Y"), x['cat']), reverse=True)
    
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("# Learning-Diary\n\n")
        
        current_date = None
        current_cat = None
        
        for e in entries:
            # Datum
            if e['date'] != current_date:
                current_date = e['date']
                f.write(f"## {current_date}\n\n")
                current_cat = None 
            
            # Kategorie: Groß und prägnant
            if e['cat'] != current_cat:
                current_cat = e['cat']
                f.write(f"### KATEGORIE: {current_cat.upper()}:\n\n")
            
            # Titel: Kleiner als Kategorie, aber deutlich
            f.write(f"**TITEL: {e['title']}**\n\n")
            
            # Details: Reiner Fließtext, klein
            f.write(f"Beschreibung: {e['desc']}  \n") # Zwei Leerzeichen am Ende für Zeilenumbruch
            f.write(f"Grund/Problem: {e['reason']}\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    try:
        data = get_input()
        all_entries = load_entries()
        all_entries.append({
            "date": data[0], "cat": data[1], "title": data[2], 
            "desc": data[3], "reason": data[4]
        })
        save_all(all_entries)
        print(f"\nErfolg: Struktur in {LOG_FILE} bereinigt.")
    except Exception as e:
        print(f"Fehler: {e}")