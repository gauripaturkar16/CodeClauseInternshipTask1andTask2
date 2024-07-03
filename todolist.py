import tkinter as tk
from tkinter import messagebox, simpledialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("650x410+300+150")

        self.tasks = []

        self.label = tk.Label(self.root, text="To-Do List App", font="Arial 25 bold", bg="orange", fg="black")
        self.label.pack(side="top", fill=tk.BOTH)

        self.task_label = tk.Label(self.root, text="Tasks",width=10, bd=5,font="Arial 18 bold", bg="orange", fg="black")
        self.task_label.place(x=280, y=54)

        self.task_listbox = tk.Listbox(self.root, height=15, width=40, bd=5, font="Arial 12 bold")
        self.task_listbox.place(x=220, y=90)

        self.text_entry = tk.Entry(self.root, bd=5, width=30, font="Arial 12 bold")
        self.text_entry.place(x=0, y=50)

        self.add_button = tk.Button(self.root, text="Add Task", font="Arial 12 bold", width=15, bg="orange", fg="black", command=self.add_task)
        self.add_button.place(x=20, y=150)

        self.edit_button = tk.Button(self.root, text="Edit Task", font="Arial 12 bold", width=15, bg="orange", fg="black", command=self.edit_task)
        self.edit_button.place(x=20, y=200)

        self.delete_button = tk.Button(self.root, text="Delete Task", font="Arial 12 bold", width=15, bg="orange", fg="black", command=self.delete_task)
        self.delete_button.place(x=20, y=250)

    def add_task(self):
        task = self.text_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.text_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task)
            if new_task:
                self.tasks[selected_index] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
