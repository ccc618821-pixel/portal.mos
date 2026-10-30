from tkinter import messagebox
def show_error(title, text, parent=None):
    messagebox.showerror(title, text, parent=parent)
def show_warning(title, text, parent=None):
    messagebox.showwarning(title, text, parent=parent)
def show_info(title, text, parent=None):
    messagebox.showinfo(title, text, parent=parent)
def ask_confirmation(title, text, parent=None):
    return messagebox.askyesno(title, text, icon=messagebox.WARNING, parent=parent)
