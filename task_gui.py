import tkinter as tk
from tkinter import messagebox, ttk
import task_db as task  # MySQL-Version

# Globale Aufgabenliste
tasks = task.load_tasks()

# --- GUI Setup ---
root = tk.Tk()
root.title("🌟 Meine To-Do App")
root.geometry("600x600")
root.configure(bg="#f9f9f9")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 12))

# --- Funktionen ---
def update_listbox(filter_mode="Alle"):
    listbox.delete(0, tk.END)

    if filter_mode == "Offen":
        filtered = [t for t in tasks if not t["completed"]]
    elif filter_mode == "Erledigt":
        filtered = [t for t in tasks if t["completed"]]
    else:
        filtered = tasks

    for t in filtered:
        status = "✔️" if t["completed"] else "❌"
        listbox.insert(tk.END, f"{t['description']}  {status}")

    # Statistik aktualisieren
    done = len([t for t in tasks if t["completed"]])
    total = len(tasks)
    stats_label.config(text=f"✅ {done} von {total} erledigt")

def add_task_gui():
    desc = task_entry.get()
    if desc:
        task.add_task(desc)
        refresh_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warnung", "Bitte eine Aufgabe eingeben!")

def mark_done_gui():
    try:
        index = listbox.curselection()[0]
        task_id = tasks[index]["id"]
        task.mark_done(task_id)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Warnung", "Bitte eine Aufgabe auswählen!")

def delete_task_gui():
    try:
        index = listbox.curselection()[0]
        task_id = tasks[index]["id"]
        task.delete_task(task_id)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Warnung", "Bitte eine Aufgabe auswählen!")

def refresh_tasks():
    global tasks
    tasks = task.load_tasks()
    update_listbox(filter_var.get())

# --- GUI Elemente ---

# Eingabe + Button
entry_frame = tk.Frame(root, bg="#f9f9f9")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=35, font=("Segoe UI", 13))
task_entry.grid(row=0, column=0, padx=5)

add_button = ttk.Button(entry_frame, text="➕ Hinzufügen", command=add_task_gui)
add_button.grid(row=0, column=1, padx=5)

# Buttons erledigen / löschen
action_frame = tk.Frame(root, bg="#f9f9f9")
action_frame.pack(pady=5)

done_button = ttk.Button(action_frame, text="✔️ Erledigt", command=mark_done_gui)
done_button.grid(row=0, column=0, padx=10)

delete_button = ttk.Button(action_frame, text="🗑️ Löschen", command=delete_task_gui)
delete_button.grid(row=0, column=1, padx=10)

# Filter
filter_frame = tk.Frame(root, bg="#f9f9f9")
filter_frame.pack(pady=5)

filter_var = tk.StringVar(value="Alle")
filter_label = tk.Label(filter_frame, text="Filter:", font=("Segoe UI", 11), bg="#f9f9f9")
filter_label.pack(side=tk.LEFT, padx=5)

filter_options = ttk.Combobox(filter_frame, textvariable=filter_var, values=["Alle", "Offen", "Erledigt"], state="readonly")
filter_options.pack(side=tk.LEFT, padx=5)
filter_options.bind("<<ComboboxSelected>>", lambda e: update_listbox(filter_var.get()))

# Aufgabenliste mit Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=55, height=18, font=("Segoe UI", 12), yscrollcommand=scrollbar.set, selectbackground="#cce5ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Statistik
stats_label = tk.Label(root, text="0 von 0 erledigt", font=("Segoe UI", 11), bg="#f9f9f9", fg="#333")
stats_label.pack(pady=5)

# Initiales Update
update_listbox()
root.mainloop()
