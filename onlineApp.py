from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import time
from os import path
import csv
import json

items = ["Nails", "Screws", "Hammer", "Electric Drill"]
sale = []
order = []

# combobox number list
numbers = list(range(6))
# place holder until inventory json/csv added
holder = 0


def close():
    win.destroy()


def clear_inputs():
    empID.set("")
    password.set("")
    sale_quantity_nails.set("0")
    sale_quantity_screws.set("0")
    sale_quantity_hammer.set("0")
    sale_quantity_electric_drill.set("0")
    order_quantity_nails.set("0")
    order_quantity_screws.set("0")
    order_quantity_hammer.set("0")
    order_quantity_electric_drill.set("0")


def verify():
    file_handle = open("employees.json")
    employee = json.load(file_handle)
    file_handle.close()

    empID = empID_entry.get()
    password = password_entry.get()

    if empID in employee:
        if password != employee[empID]["Password"]:
            clear_inputs()
            messagebox.showwarning("Error", "Check Employee ID or Password")
        else:
            pass_frame.grid_forget()
            option_frame.grid(row=2, column=0, padx=10, pady=10)
    else:
        clear_inputs()
        messagebox.showwarning("Error", "Check Employee ID or Password")


def sales():
    option_frame.grid_forget()
    sales_frame.grid(row=2, column=0, padx=10, pady=10)


def sale_submit():
    clear_inputs()


def orders():
    option_frame.grid_forget()
    orders_frame.grid(row=2, column=0, padx=10, pady=10)


def order_submit():
    clear_inputs()

def cancel():
    option_frame.grid_forget()
    cancel_frame.grid(row=2, column=0, padx=10, pady=10)

def cancel_ID():
    clear_inputs()

def back_to_option_from_cancel():
    cancel_frame.grid_forget()
    option_frame.grid(row=2, column=0, padx=10, pady=10)


def back_to_option_from_sales():
    sales_frame.grid_forget()
    option_frame.grid(row=2, column=0, padx=10, pady=10)


def back_to_option_from_orders():
    orders_frame.grid_forget()
    option_frame.grid(row=2, column=0, padx=10, pady=10)


win = Tk()
win.title("Engage Business")
win.resizable(False, False)
win.config(bg="green")

# main_frame
main_frame = Frame(win, width=700, height=700, bg="light green")
main_frame.grid(row=0, column=0, padx=10, pady=10)

# image
logo = Image.open("engageBusiness.jpg")
new_width = 200
new_height = 150
img = logo.resize((new_width, new_height), Image.ANTIALIAS)
img.save("engageBusiness.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(main_frame, image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0, pady=10)

# exit button
exit_button = Button(main_frame, command=close, text="Exit")
exit_button.grid(column=0, row=3, padx=10, pady=10)

# pass_fram for empID/password input
pass_frame = Frame(main_frame, width=680, height=680)
pass_frame.grid(row=2, column=0, padx=10, pady=10)

box1 = Frame(pass_frame, bg="white", width=280, height=100, borderwidth=5, relief=RIDGE)
box1.grid(row=0, columnspan=3, ipady=5, pady=5)
box1.grid_propagate(False)
box1.rowconfigure(0, weight=1)
box1.rowconfigure(1, weight=1)
box1.rowconfigure(2, weight=1)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=1)

# empID input
empID_label = Label(box1, text="Employee ID:")
empID_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

empID = StringVar()
empID_entry = Entry(box1, textvariable=empID)
empID_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password input
password_label = Label(box1, text="Password:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

password = StringVar()
password_entry = Entry(box1, textvariable=password, show="*")
password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# login button
login_button = Button(box1, command=verify, text="Login")
login_button.grid(column=1, row=2, sticky=E, padx=5, pady=5)

# action option frame
option_frame = Frame(main_frame, width=680, height=680)

# box 2 for action option
box2 = Frame(option_frame, bg="white", width=300, height=100, borderwidth=5, relief=RIDGE)
box2.grid(row=0, columnspan=3, ipady=5, pady=5)
box2.grid_propagate(False)
box2.rowconfigure(0, weight=1)
box2.columnconfigure(0, weight=1)
box2.columnconfigure(1, weight=1)
box2.columnconfigure(2, weight=1)

# sales option
sales_button = Button(box2, command=sales, width=90, height=80, text="Sale")
sales_button.grid(column=0, row=0, padx=10, pady=10)

# order option
orders_button = Button(box2, command=orders, width=90, height=80, text="Order")
orders_button.grid(column=1, row=0, padx=10, pady=10)

# cancel option
cancel_button = Button(box2, command=cancel, width=90, height=80, text="Cancel")
cancel_button.grid(column=2, row=0, padx=10, pady=10)

# sales frame
sales_frame = Frame(main_frame, width=680, height=680)

# box 3 for sales
box3 = Frame(sales_frame, bg="white", width=450, height=200, borderwidth=5, relief=RIDGE)
box3.grid(row=0, columnspan=3, ipady=5, pady=5)
box3.grid_propagate(False)
box3.rowconfigure(0, weight=1)
box3.rowconfigure(1, weight=1)
box3.rowconfigure(2, weight=1)
box3.rowconfigure(3, weight=1)
box3.rowconfigure(4, weight=1)
box3.rowconfigure(5, weight=1)
box3.columnconfigure(0, weight=1)
box3.columnconfigure(1, weight=1)
box3.columnconfigure(2, weight=1)

# sales amount for each item
amount_sale_label = Label(box3, text="Amount to sale:")
amount_sale_label.grid(column=0, row=0, padx=5)

sale_quantity_nails = IntVar()
amount_sale_combobox_nails = ttk.Combobox(box3, textvariable=sale_quantity_nails, values=numbers, state="readonly")
amount_sale_combobox_nails.grid(column=0, row=1, padx=5, pady=5)

sale_quantity_screws = IntVar()
amount_sale_combobox_screws = ttk.Combobox(box3, textvariable=sale_quantity_screws, values=numbers, state="readonly")
amount_sale_combobox_screws.grid(column=0, row=2, padx=5, pady=5)

sale_quantity_hammer = IntVar()
amount_sale_combobox_hammer = ttk.Combobox(box3, textvariable=sale_quantity_hammer, values=numbers, state="readonly")
amount_sale_combobox_hammer.grid(column=0, row=3, padx=5, pady=5)

sale_quantity_electric_drill = IntVar()
amount_sale_combobox_electric_drill = ttk.Combobox(box3, textvariable=sale_quantity_electric_drill, values=numbers, state="readonly")
amount_sale_combobox_electric_drill.grid(column=0, row=4, padx=5, pady=5)

# sales item for each item
sale_item_label = Label(box3, text="Item:")
sale_item_label.grid(column=1, row=0, padx=5)

sale_item_nails_label = Label(box3, text="Nails")
sale_item_nails_label.grid(column=1, row=1, padx=5, pady=5)

sale_item_screws_label = Label(box3, text="Screws")
sale_item_screws_label.grid(column=1, row=2, padx=5, pady=5)

sale_item_hammer_label = Label(box3, text="Hammer")
sale_item_hammer_label.grid(column=1, row=3, padx=5, pady=5)

sale_item_elecric_drill_label = Label(box3, text="Electric Drill")
sale_item_elecric_drill_label.grid(column=1, row=4, padx=5, pady=5)

# sales inventory for each amount will link to csv/json for updated numbers
sale_inventory_amount_label = Label(box3, text="Amount in Inventory:")
sale_inventory_amount_label.grid(column=2, row=0, padx=5)

sale_inventory_nails_label = Label(box3, text=f"{holder}")
sale_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

sale_inventory_screws_label = Label(box3, text=f"{holder}")
sale_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

sale_inventory_hammer_label = Label(box3, text=f"{holder}")
sale_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

sale_inventory_elecric_drill_label = Label(box3, text=f"{holder}")
sale_inventory_elecric_drill_label.grid(column=2, row=4, padx=5, pady=5)

# submit sale button for total
sale_submit_button = Button(box3, command=sale_submit, text="Submit")
sale_submit_button.grid(column=2, row=5, padx=5, pady=5)

# back button
sales_back_button = Button(box3, command=back_to_option_from_sales, text="Back")
sales_back_button.grid(column=0, row=5, padx=5, pady=5)

# order frame
orders_frame = Frame(main_frame, width=680, height=680)

# box 4 for sales
box4 = Frame(orders_frame, bg="white", width=450, height=200, borderwidth=5, relief=RIDGE)
box4.grid(row=0, columnspan=3, ipady=5, pady=5)
box4.grid_propagate(False)
box4.rowconfigure(0, weight=1)
box4.rowconfigure(1, weight=1)
box4.rowconfigure(2, weight=1)
box4.rowconfigure(3, weight=1)
box4.rowconfigure(4, weight=1)
box4.rowconfigure(5, weight=1)
box4.columnconfigure(0, weight=1)
box4.columnconfigure(1, weight=1)
box4.columnconfigure(2, weight=1)

# order amount for each item
amount_order_label = Label(box4, text="Amount to Order:")
amount_order_label.grid(column=0, row=0, padx=5)

order_quantity_nails = IntVar()
amount_order_combobox_nails = ttk.Combobox(box4, textvariable=order_quantity_nails, values=numbers, state="readonly")
amount_order_combobox_nails.grid(column=0, row=1, padx=5, pady=5)

order_quantity_screws = IntVar()
amount_order_combobox_screws = ttk.Combobox(box4, textvariable=order_quantity_screws, values=numbers, state="readonly")
amount_order_combobox_screws.grid(column=0, row=2, padx=5, pady=5)

order_quantity_hammer = IntVar()
amount_order_combobox_hammer = ttk.Combobox(box4, textvariable=order_quantity_hammer, values=numbers, state="readonly")
amount_order_combobox_hammer.grid(column=0, row=3, padx=5, pady=5)

order_quantity_electric_drill = IntVar()
amount_order_combobox_electric_drill = ttk.Combobox(box4, textvariable=order_quantity_electric_drill, values=numbers, state="readonly")
amount_order_combobox_electric_drill.grid(column=0, row=4, padx=5, pady=5)

# order item for each item
order_item_label = Label(box4, text="Item:")
order_item_label.grid(column=1, row=0, padx=5)

order_item_nails_label = Label(box4, text="Nails")
order_item_nails_label.grid(column=1, row=1, padx=5, pady=5)

order_item_screws_label = Label(box4, text="Screws")
order_item_screws_label.grid(column=1, row=2, padx=5, pady=5)

order_item_hammer_label = Label(box4, text="Hammer")
order_item_hammer_label.grid(column=1, row=3, padx=5, pady=5)

order_item_elecric_drill_label = Label(box4, text="Electric Drill")
order_item_elecric_drill_label.grid(column=1, row=4, padx=5, pady=5)

# order inventory for each amount will link to csv/json for updated numbers
order_inventory_amount_label = Label(box4, text="Amount in Inventory:")
order_inventory_amount_label.grid(column=2, row=0, padx=5)

order_inventory_nails_label = Label(box4, text=f"{holder}")
order_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

order_inventory_screws_label = Label(box4, text=f"{holder}")
order_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

order_inventory_hammer_label = Label(box4, text=f"{holder}")
order_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

order_inventory_elecric_drill_label = Label(box4, text=f"{holder}")
order_inventory_elecric_drill_label.grid(column=2, row=4, padx=5, pady=5)

# oder submit button
order_submit_button = Button(box4, command=order_submit, text="Submit")
order_submit_button.grid(column=2, row=5, padx=5, pady=5)

# back button
order_back_button = Button(box4, command=back_to_option_from_orders, text="Back")
order_back_button.grid(column=0, row=5, padx=5, pady=5)

# cancel frame
cancel_frame = Frame(main_frame, width=680, height=680)

# box 5 for cancels
box5 = Frame(cancel_frame, bg="white", width=280, height=100, borderwidth=5, relief=RIDGE)
box5.grid(row=0, columnspan=3, ipady=5, pady=5)
box5.grid_propagate(False)
box5.rowconfigure(0, weight=1)
box5.rowconfigure(1, weight=1)
box5.rowconfigure(2, weight=1)
box5.columnconfigure(0, weight=1)
box5.columnconfigure(1, weight=1)


cancel_label = Label(box5, text="Enter Order/Sale ID:")
cancel_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

ID = StringVar()
cancel_entry = Entry(box5, textvariable=ID)
cancel_entry.grid(column=1, row=0, padx=5, pady=5)

cancel_button = Button(box5, command=cancel_ID, text="Cancel")
cancel_button.grid(column=1, row=1, padx=5, pady=5)

# back button
order_back_button = Button(box5, command=back_to_option_from_cancel, text="Back")
order_back_button.grid(column=0, row=1, padx=5, pady=5)


win.mainloop()
