from tkinter import *
from screens import render_main_screen

if __name__ == '__main__':
    tk = Tk()
    tk.geometry('800x800', )
    tk.title('My GUI Product Shop')
    render_main_screen(tk)
    tk.mainloop()
