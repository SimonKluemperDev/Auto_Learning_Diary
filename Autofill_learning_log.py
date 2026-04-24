import os
import json
from datetime import datetime

BASE_DIR = r"C:\Users\HomeTN\Documents\Klümper\learning-log.md"                                            # Path configuration - using raw string for Windows compatibility
LOG_FILE = os.path.join(BASE_DIR, "DIARY.md")
DATA_FILE = os.path.join(BASE_DIR, ".data.json")

def get_input():
    """Captures user input and ensures directory existence."""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    
    print("--- New Entry ---")
    category = input("Category: ").strip()
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    reason = input("Why/Problem: ").strip()
    
    if not category or not title:                                                                         # Validation: Ensuring structural integrity of the database
        raise ValueError("Category and Title cannot be empty.")
        
    date_str = datetime.now().strftime("%d.%m.%Y")
    return date_str, category, title, description, reason

def load_entries():
    """Reads historical data from JSON. Returns empty list if file is missing or corrupt."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError: 
            return []                                                                                   # Fail-safe against corrupted JSON
    return []

def save_all(entries):
    """Primary logic: Updates JSON database and exports formatted Markdown."""

    with open(DATA_FILE, "w", encoding="utf-8") as f:                                                   # 1. Update the 'Database' (JSON) first
        json.dump(entries, f, indent=4)
    
    
    
    entries.sort(key=lambda x: (datetime.strptime(x['date'], "%d.%m.%Y"), x['cat'].lower()), reverse=True)      # 2. Sort logic: Convert string back to datetime object for correct chronological order
                                                                                                        # Then sort by category as a secondary criterion
   
    with open(LOG_FILE, "w", encoding="utf-8") as f:                                                    # 3. Generate the human-readable Markdown export
        f.write("# Learning Diary\n\n")
        
        current_date = None
        current_cat = None
        
        for e in entries:
            if e['date'] != current_date:                                                               # Grouping logic: Only print date/category headers when they change
                current_date = e['date']
                f.write(f"## {current_date}\n\n")
                current_cat = None 
            
            if e['cat'].lower() != (current_cat.lower() if current_cat else None):
                current_cat = e['cat']
                f.write(f"### Category: {current_cat.capitalize()}\n\n")
            
            f.write(f"**Title: {e['title']}**\n\n")
            f.write(f"Description: {e['desc']}  \n")
            f.write(f"Reason/Problem: {e['reason']}\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    """Entry point: Manages the application flow and error handling."""
    try:
        data = get_input()                                                                      
        all_entries = load_entries()
        
        all_entries.append({
            "date": data[0], 
            "cat": data[1], 
            "title": data[2], 
            "desc": data[3], 
            "reason": data[4]
        })
        
        save_all(all_entries)
        print(f"\nSuccess: Diary updated in {LOG_FILE}.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
