import tkinter as tk
from tkinter import messagebox

# --- Functions ---
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def mark_done():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        if not task.startswith("✅ "):
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, f"✅ {task}")
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to mark as done.")

# --- Main Window ---
root = tk.Tk()
root.title("iOS-Style To-Do List")
root.geometry("350x500")
root.configure(bg="#f0f0f5")  # Light iOS-style background
root.resizable(False, False)

# --- Header ---
header = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 24, "bold"), bg="#f0f0f5")
header.pack(pady=10)

# --- Task Entry ---
task_frame = tk.Frame(root, bg="#f0f0f5")
task_frame.pack(pady=10)

task_entry = tk.Entry(task_frame, font=("Helvetica", 16), width=20, bd=0, relief=tk.FLAT)
task_entry.pack(side=tk.LEFT, padx=(10,5), ipady=5)

add_button = tk.Button(task_frame, text="Add", font=("Helvetica", 14), bg="#007AFF", fg="white",
                       bd=0, relief=tk.FLAT, padx=15, command=add_task)
add_button.pack(side=tk.LEFT)

# --- Task List ---
tasks_listbox = tk.Listbox(root, font=("Helvetica", 16), bg="white", fg="black", bd=0,
                           selectbackground="#007AFF", selectforeground="white")
tasks_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Action Buttons ---
action_frame = tk.Frame(root, bg="#f0f0f5")
action_frame.pack(pady=10)

done_button = tk.Button(action_frame, text="✅ Done", font=("Helvetica", 14), bg="#34C759", fg="white",
                        bd=0, relief=tk.FLAT, padx=15, command=mark_done)
done_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(action_frame, text="🗑 Delete", font=("Helvetica", 14), bg="#FF3B30", fg="white",
                          bd=0, relief=tk.FLAT, padx=15, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# --- Run App ---
root.mainloop()
