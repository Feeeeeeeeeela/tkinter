from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.first= tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, background="red")
        self.first.grid(row=0, column=0)

        self.second = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, background="green")
        self.second.grid(row=0, column=1)

        self.third = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, background="blue")
        self.third.grid(row=0, column=2)

        self.canv = tk.Canvas(background="#000000")
        self.canv.grid(row=1, column=0, columnspan=3)

        self.btn = tk.Button(self, text="jo", command=lambda:self.onpress())
        self.btn.grid(row=2, column=0, columnspan=3)

    def onpress(self, event=None):
        rn = self.first.get()
        gn = self.second.get()
        bn = self.third.get()
        hexnumber = '#%02x%02x%02x' % (rn, gn, bn)
        self.canv.configure(bg = hexnumber)


app = Application()
app.geometry("600x500")
app.mainloop()
