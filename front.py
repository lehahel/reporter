import tkinter as tk
from generator import *


def start_app():
    tk_main = tk.Tk()
    app = Application(tk_main)
    tk_main.mainloop()


class Application(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.report = Report()

        self.add_name_button = tk.Button(text='Добавить имя', width=25)
        self.add_name_button.config(command=self.add_name_window)
        self.add_name_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.add_point_button = tk.Button(text='Добавить пункт', width=25)
        self.add_point_button.config(command=self.add_point_window)
        self.add_point_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        self.add_ticket_button = tk.Button(text='Добавить тикет', width=25)
        self.add_ticket_button.config(command=self.add_ticket_window)
        self.add_ticket_button.grid(row=1, column=4, columnspan=2, padx=10, pady=10)

        self.text_box = tk.Text(width=100, height=25, bg='lightblue', wrap=tk.WORD)
        self.text_box.grid(row=5, columnspan=10, padx=10, pady=10)

    def add_point(self, toplevel, text):
        toplevel.destroy()
        toplevel.update()
        self.report.add_point(description=text)
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, str(self.report))

    def add_point_window(self):
        t = tk.Toplevel(self)
        tk.Label(t, text='Введите заголовок', width=20, height=10).grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        point_text = tk.Text(t, width=30, height=10, bg='lightblue')
        point_text.grid(row=1, column=3, columnspan=3, padx=10, pady=10)
        button = tk.Button(t, text='Добавить', width=10, height=10)
        button.config(command=lambda: self.add_point(t, point_text.get('1.0', tk.END)))
        button.grid(row=1, column=8, padx=10, pady=10)

    def add_ticket(self, toplevel, point, ticket):
        toplevel.destroy()
        toplevel.update()
        if not point.strip().isdigit():
            return
        self.report.add_ticket(point=int(point.strip()), ticket=ticket)
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, str(self.report))

    def add_ticket_window(self):
        t = tk.Toplevel(self)
        tk.Label(t, text='Введите номер пункта', width=20, height=5).grid(
            row=1, column=1, columnspan=2, padx=10, pady=10
        )
        tk.Label(t, text='Введите номер пункта', width=20, height=5).grid(
            row=2, column=1, columnspan=2, padx=10, pady=10
        )
        point_text = tk.Text(t, width=30, height=5, bg='lightblue')
        point_text.grid(row=1, column=3, columnspan=3, padx=10, pady=10)
        ticket_text = tk.Text(t, width=30, height=5, bg='lightblue')
        ticket_text.grid(row=2, column=3, columnspan=3, padx=10, pady=10)
        button = tk.Button(t, text='Добавить', width=10, height=5)
        button.config(command=lambda: self.add_ticket(t, point_text.get('1.0', tk.END), ticket_text.get('1.0', tk.END)))
        button.grid(row=1, column=8, padx=10, pady=20)

    def add_name_text(self, toplevel, name):
        toplevel.destroy()
        toplevel.update()
        self.report.change_name(name=name)
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, str(self.report))

    def add_name_window(self):
        t = tk.Toplevel(self)
        tk.Label(t, text='Введите имя отчета', width=20, height=5).grid(
            row=1, column=1, columnspan=2, padx=10, pady=10
        )
        name_text = tk.Text(t, width=30, height=5, bg='lightblue')
        name_text.grid(row=1, column=3, columnspan=3, padx=10, pady=10)
        button = tk.Button(t, text='Добавить', width=11, height=5)
        button.config(command=lambda: self.add_name_text(t, name_text.get('1.0', tk.END)))
        button.grid(row=1, column=8, padx=10, pady=20)
