import tkinter.messagebox
from tkinter import *


class Calculatrice(Frame):

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        self.expression = StringVar()
        self.expression.set("hello")
        self.non_expression = True

        # création des widgets

        # # Menu
        self.menubar = Menu(self)
        self.menubar.add_command(label="aide",
                                 command=lambda: tkinter.messagebox.showinfo(message="Membre premium only"))
        self.menubar.add_command(label="mode calculatrice",
                                 command=lambda: tkinter.messagebox.showinfo(message="Membre premium only"))

        # # Conteneurs
        self.frame_nombre = Frame(self)
        self.frame_nombre.pack(side=BOTTOM, fill=BOTH)
        self.frame_result = Frame(self)
        self.frame_result.pack(side=TOP, fill=Y)

        # # Nombres
        for i in range(7, 10):
            Button(self.frame_nombre, text=i.__str__(),
                   command=lambda ops=i: self.fct_number(ops), width=4).grid(row=1, column=i - 7)
        for i in range(4, 7):
            Button(self.frame_nombre, text=i.__str__(),
                   command=lambda ops=i: self.fct_number(ops), width=4).grid(row=2, column=i - 4)
        for i in range(1, 4):
            Button(self.frame_nombre, text=i.__str__(),
                   command=lambda ops=i: self.fct_number(ops), width=4).grid(row=3, column=i - 1)
        Button(self.frame_nombre, text="0", command=lambda ops=0: self.fct_number(ops), width=4).grid(row=4, column=1)
        Button(self.frame_nombre, text=".", command=lambda ops=".": self.fct_number(ops), width=4).grid(row=4, column=2)
        Button(self.frame_nombre, text="**", command=lambda ops="**": self.fct_number(ops), width=4).grid(row=4,
                                                                                                          column=0)

        # # Opérateurs
        Button(self.frame_nombre, text="C", command=lambda ops="C": self.fct_c(), width=5).grid(row=1, column=4,
                                                                                                padx=20)
        Button(self.frame_nombre, text="AC", command=lambda ops="AC": self.fct_ac(), width=5).grid(row=1, column=5)
        Button(self.frame_nombre, text="+", command=lambda ops="+": self.fct_number(ops), width=5).grid(row=2, column=4,
                                                                                                        padx=20)
        Button(self.frame_nombre, text="-", command=lambda ops="-": self.fct_number(ops), width=5).grid(row=2, column=5)
        Button(self.frame_nombre, text="/", command=lambda ops="/": self.fct_number(ops), width=5).grid(row=3, column=4,
                                                                                                        padx=20)
        Button(self.frame_nombre, text="*", command=lambda ops="*": self.fct_number(ops), width=5).grid(row=3, column=5)
        Button(self.frame_nombre, text="=", command=lambda ops="=": self.fct_equals(), width=5).grid(row=4, column=4)
        Button(self.frame_nombre, text="(", command=lambda ops="(": self.fct_number(ops), width=5).grid(row=2, column=6)
        Button(self.frame_nombre, text=")", command=lambda ops=")": self.fct_number(ops), width=5).grid(row=3, column=6)
        self.result = Label(self.frame_result, textvariable=self.expression, relief=RIDGE, width=25, anchor=E,
                            pady=10).pack()

    # Fonction
    def fct_number(self, ops):
        self.check_non_expression()
        self.expression.set(self.expression.get() + str(ops))

    def fct_c(self):
        self.check_non_expression()
        expression_local = self.expression.get()
        expression_local = expression_local[:-1]
        self.expression.set(expression_local)

    def fct_ac(self):
        self.expression.set("")

    def fct_equals(self):
        try:
            result = eval(self.expression.get())
        except ZeroDivisionError:
            self.expression.set("Division par 0")
        except SyntaxError:
            self.expression.set("Expression incorrect")
        else:
            self.expression.set(result)
        finally:
            self.non_expression = True

    def check_non_expression(self):
        if self.non_expression:
            self.expression.set("")
            self.non_expression = False


class MyDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)

        Label(top, text="Accès membre premium seulement").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.top.destroy()


if __name__ == "__main__":
    _window = Tk()
    _window.config(menu=Calculatrice(_window, height=50, width=30, padx=5).menubar)
    _window.mainloop()
