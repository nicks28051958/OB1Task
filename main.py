import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=0, column=0)
        self.description_entry = tk.Entry(root, width=50)
        self.description_entry.grid(row=0, column=1, columnspan=2)

        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.due_date_label.grid(row=1, column=0)
        self.due_date_entry = tk.Entry(root, width=50)
        self.due_date_entry.grid(row=1, column=1, columnspan=2)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=3)

        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.grid(row=3, column=0, columnspan=2)

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.grid(row=3, column=2)

        self.refresh_tasks()

    def add_task(self):
        description = self.description_entry.get()
        due_date_str = self.due_date_entry.get()

        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Due date must be in YYYY-MM-DD format")
            return

        task = Task(description, due_date)
        self.tasks.append(task)
        self.refresh_tasks()

    def mark_completed(self):
        selected_index = self.tasks_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No task selected")
            return

        task_index = selected_index[0]
        self.tasks[task_index].mark_completed()
        self.refresh_tasks()

    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            if not task.completed:
                task_str = f"{task.description} (Due: {task.due_date.strftime('%Y-%m-%d')})"
                self.tasks_listbox.insert(tk.END, task_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
