import mysql.connector

# Verbindung zur Datenbank
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # der Standard-User
    password="",       # dein root-Passwort (leer lassen, wenn keins gesetzt wurde)
    database="ToDoList"
)


cursor = conn.cursor(dictionary=True)

def load_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    return cursor.fetchall()

def add_task(desc):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (%s, 0)", (desc,))
    conn.commit()

def mark_done(task_id):
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=%s", (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
