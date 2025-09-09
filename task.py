import json
import os

# Datei für Speicherung
FILE_NAME = 'tasks.json'

# Funktion zum Laden der Aufgaben
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        # Falls Datei nicht existiert → leere Liste zurückgeben und Datei anlegen
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
        return []

# Funktion zum Speichern der Aufgaben
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

# Funktion zum Hinzufügen einer Aufgabe
def add_task(description):
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print(f"✅ Aufgabe hinzugefügt: {description}")

# Funktion zum Anzeigen der Aufgaben
def list_tasks():
    if not tasks:
        print("📂 Keine Aufgaben vorhanden.")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["completed"] else "❌"
        print(f"{i}. {t['description']} [{status}]")

# Funktion zum Markieren einer Aufgabe als erledigt
def mark_done(index):
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✔️ Aufgabe erledigt: {tasks[index - 1]['description']}")
    except IndexError:
        print("⚠️ Ungültige Aufgaben-Nummer!")

# Funktion zum Löschen einer Aufgabe
def delete_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Aufgabe gelöscht: {removed_task['description']}")
    except IndexError:
        print("⚠️ Ungültige Aufgaben-Nummer!")

# Hauptprogramm
if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe erledigen")
        print("4. Aufgabe löschen")
        print("5. Beenden")

        choice = input("👉 Wähle eine Option: ")
            
        if choice == '1':
            desc = input("Neue Aufgabe: ")
            add_task(desc)   # ✅ korrigiert
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks()
            try:
                i = int(input("Nummer der zu erledigenden Aufgabe: "))
                mark_done(i)
            except ValueError:
                print("⚠️ Bitte eine Zahl eingeben.")
        elif choice == '4':
            list_tasks()
            try:
                i = int(input("Nummer der zu löschenden Aufgabe: "))
                delete_task(i)
            except ValueError:
                print("⚠️ Bitte eine Zahl eingeben.")
        elif choice == '5':
            print("👋 Auf Wiedersehen!")
            break
        else:
            print("⚠️ Ungültige Option, bitte erneut versuchen.")
