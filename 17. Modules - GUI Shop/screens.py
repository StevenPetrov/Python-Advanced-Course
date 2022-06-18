from tkinter import *

import cl as cl
import tk as tk
from PIL import Image, ImageTk

from auth_service import register, login
from product_service import get_all_projects
from PIL import *


def clear_window(tk):
    for widget in tk.winfo_children():
        widget.destroy()


def render_main_screen(tk):
    Button(tk, text='Login', bg='green', command=lambda: render_login_screen(tk)).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=lambda: render_register_screen(tk)).grid(row=0, column=1)


def render_register_screen(tk):
    clear_window(tk)
    Label(tk, text='Email').grid(row=0, column=0)
    email_entry = Entry(tk)
    email_entry.grid(row=0, column=1)

    Label(tk, text='Password', ).grid(row=1, column=0)
    password_entry = Entry(tk, show='*')
    password_entry.grid(row=1, column=1)

    Label(tk, text='Confirm Password').grid(row=2, column=0)
    confirmed_password_entry = Entry(tk, show='*')
    confirmed_password_entry.grid(row=2, column=1)

    def on_register():
        email = email_entry.get()
        password = password_entry.get()
        confirmed_password = confirmed_password_entry.get()

        if password != confirmed_password:
            Label(tk, text='Password must match').grid(row=3, column=1)
            return
        result = register(email, password)
        if result:
            render_login_screen(tk)
        else:
            Label(tk, text='Email is already registered!').grid(row=3, column=1)

    Button(tk, text='Register', command=lambda: on_register()).grid(row=4, column=1)


def render_login_screen(tk):
    clear_window(tk)
    Label(tk, text='Email').grid(row=0, column=0)
    email_entry = Entry(tk)
    email_entry.grid(row=0, column=1)

    Label(tk, text='Password', ).grid(row=1, column=0)
    password_entry = Entry(tk, show='*')
    password_entry.grid(row=1, column=1)

    def on_login():
        email = email_entry.get()
        password = password_entry.get()

        result = login(email, password)
        if result:
            render_products_screens(tk)
        else:
            Label(tk, text='Wrong credentials!', fg='red').grid(row=2, column=1)

    Button(tk, text='Login', command=lambda: on_login()).grid(row=3, column=1)


def render_products_screens(tk):
    clear_window(tk)
    col = 0
    row = 0
    products = get_all_projects()
    for product in products:
        if col % 3 == 0:
            row += 4
            col = 0
        Label(tk, text=product['name']).grid(row=row, column=col)

        photo = Image.open(f"./products/{product['imgPath']}")
        photo = photo.resize((160,160))
        img = ImageTk.PhotoImage(photo)
        img_label = Label(tk,image=img)
        img_label.image=img
        img_label.grid(row=row+1, column=col)


        Label(tk, text=product['count']).grid(row=row+2, column=col)

        Button(tk, text='Buy').grid(row=row+3, column=col)
        col +=1