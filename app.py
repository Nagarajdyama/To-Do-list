import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()
clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks)
clear_button.pack()

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=15)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()
