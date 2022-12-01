from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import time
from os import path
import csv
import json

# combobox number list
numbers = list(range(6))
# global number for order placeing
num = 0

# 
def close():
    win.destroy()


def clear_inputs():
    empID.set("")
    password.set("")
    quantity_nails.set("0")
    quantity_screws.set("0")
    quantity_hammer.set("0")
    quantity_electric_drill.set("0")
    ID.set("")


def verify():
    file_handle = open("employees.json")
    employee = json.load(file_handle)
    file_handle.close()

    empID = empID_entry.get()
    password = password_entry.get()

    if empID in employee:
        if password != employee[empID]["Password"]:
            clear_inputs()
            messagebox.showwarning(title= "Credential Error", message= "Check Employee ID or Password")
        else:
            pass_frame.grid_forget()
            option_frame.grid(row=2, column=0, padx=10, pady=10)
    else:
        clear_inputs()
        messagebox.showwarning(title= "Credential Error", message= "Check Employee ID or Password")


def log_transaction(transaction_num, q_nails, q_screws, q_hammer, q_electric_drill, total):
    if not path.isfile("transactions.csv"):
        with open("transactions.csv", "w", newline='') as fp:
            data = csv.writer(fp)
            data.writerow(["Transaction Number", "Time", "Nails", "Screws", "Hammers", "Electric Drills", "Total"])
    
    with open("transactions.csv", "a", newline='') as fp:
        data = csv.writer(fp)
        data.writerow([transaction_num, time.ctime(), q_nails, q_screws, q_hammer, q_electric_drill, f'${total:0.2f}'])


def sales():
    option_frame.grid_forget()
    sales_frame.grid(row=2, column=0, padx=10, pady=10)


def update():
    file_handle = open("inventory.json")
    inventory = json.load(file_handle)
    file_handle.close()

    #sales
    sale_inventory_nails_label = Label(box3, text=f"{inventory['Nails']['quantity']}")
    sale_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

    sale_inventory_screws_label = Label(box3, text=f"{inventory['Screws']['quantity']}")
    sale_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

    sale_inventory_hammer_label = Label(box3, text=f"{inventory['Hammer']['quantity']}")
    sale_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

    sale_inventory_elecric_drill_label = Label(box3, text=f"{inventory['Electric Drill']['quantity']}")
    sale_inventory_elecric_drill_label.grid(column=2, row=4, padx=5, pady=5)

    #orders
    order_inventory_nails_label = Label(box4, text=f"{inventory['Nails']['quantity']}")
    order_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

    order_inventory_screws_label = Label(box4, text=f"{inventory['Screws']['quantity']}")
    order_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

    order_inventory_hammer_label = Label(box4, text=f"{inventory['Hammer']['quantity']}")
    order_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

    order_inventory_elecric_drill_label = Label(box4, text=f"{inventory['Electric Drill']['quantity']}")
    order_inventory_elecric_drill_label.grid(column=2, row=4, padx=5, pady=5)

    win.after(1000, update)


def sale_submit():
    file_handle = open("inventory.json")
    inventory = json.load(file_handle)
    file_handle.close()
    
    q_nails = quantity_nails.get()
    q_screws = quantity_screws.get()
    q_hammer = quantity_hammer.get()
    q_electric_drill = quantity_electric_drill.get()

    if q_nails > inventory["Nails"]["quantity"]:
        messagebox.showwarning(title= "Inventory Error", message= "Not enough Nails to sell")
        clear_inputs()
    elif q_screws > inventory["Screws"]["quantity"]:
        messagebox.showwarning(title= "Inventory Error", message= "Not enough Screws to sell")
        clear_inputs()
    elif q_hammer > inventory["Hammer"]["quantity"]:
        messagebox.showwarning(title= "Inventory Error", message= "Not enough Hammers to sell")
        clear_inputs()
    elif q_electric_drill > inventory["Electric Drill"]["quantity"]:
        messagebox.showwarning(title= "Inventory Error", message= "Not enough Electric Drills to sell")
        clear_inputs()
    else:
        sale_nails = inventory["Nails"]["sale price"] * q_nails
        sale_screws = inventory["Screws"]["sale price"] * q_screws
        sale_hammer = inventory["Hammer"]["sale price"] * q_hammer
        sale_electric_drill = inventory["Electric Drill"]["sale price"] * q_electric_drill

        sale_pre_total = (sale_nails + sale_screws + sale_hammer + sale_electric_drill)

        sales_tax = sale_pre_total * 0.086

        total = sale_pre_total + sales_tax
        
        global num
        num += 1
        num_fill = str(num).zfill(4)
        transaction_num = f'S{num_fill}'

        log_transaction(transaction_num, q_nails, q_screws, q_hammer, q_electric_drill, total)

        inventory["Nails"]["quantity"] = inventory["Nails"]["quantity"] - q_nails
        inventory["Screws"]["quantity"] = inventory["Screws"]["quantity"] - q_screws
        inventory["Hammer"]["quantity"] = inventory["Hammer"]["quantity"] - q_hammer
        inventory["Electric Drill"]["quantity"] = inventory["Electric Drill"]["quantity"] - q_electric_drill
        
            
        messagebox.showinfo(title="Sales Total", 
                            message= f"Total: ${sale_pre_total:0.2f}\nTax: ${sales_tax:0.2f}\nSales Total: ${total:0.2f}")

        with open('inventory.json', 'w') as file_handle:
            json.dump(inventory, file_handle)
        
        clear_inputs()

        update()
        

def orders():
    option_frame.grid_forget()
    orders_frame.grid(row=2, column=0, padx=10, pady=10)


def order_submit():
    file_handle = open("inventory.json")
    inventory = json.load(file_handle)
    file_handle.close()

    q_nails = quantity_nails.get()
    q_screws = quantity_screws.get()
    q_hammer = quantity_hammer.get()
    q_electric_drill = quantity_electric_drill.get()

    order_nails = inventory["Nails"]["order price"] * q_nails
    order_screws = inventory["Screws"]["order price"] * q_screws
    order_hammer = inventory["Hammer"]["order price"] * q_hammer
    order_electric_drill = inventory["Electric Drill"]["order price"] * q_electric_drill

    order_pre_total = (order_nails + order_screws + order_hammer + order_electric_drill)

    order_tax = order_pre_total * 0.086

    order_shipping = order_pre_total * 1.086

    total = order_pre_total + order_tax + order_shipping

    global num
    num += 1
    num_fill = str(num).zfill(4)
    transaction_num = f'O{num_fill}'    

    log_transaction(transaction_num, q_nails, q_screws, q_hammer, q_electric_drill, total)

    inventory["Nails"]["quantity"] = inventory["Nails"]["quantity"] + q_nails
    inventory["Screws"]["quantity"] = inventory["Screws"]["quantity"] + q_screws
    inventory["Hammer"]["quantity"] = inventory["Hammer"]["quantity"] + q_hammer
    inventory["Electric Drill"]["quantity"] = inventory["Electric Drill"]["quantity"] + q_electric_drill

    messagebox.showinfo(title="Order Total",
                        message= f"Total: ${order_pre_total:0.2f}\nTax: ${order_tax:0.2f}\nShipping: ${order_shipping:0.2f}\nOrder Total: ${total:0.2f}")
    
    with open('inventory.json', 'w') as file_handle:
        json.dump(inventory, file_handle)

    clear_inputs()

    update()


def cancel():
    option_frame.grid_forget()
    cancel_frame.grid(row=2, column=0, padx=10, pady=10)


def update_inventory():
    file_handle = open("inventory.json")
    inventory = json.load(file_handle)
    file_handle.close()


    with open('transactions.csv', 'r', newline='') as fp:
        for row in csv.reader(fp):
            if row[0] == ID.get():
                if "O" in ID.get():
                    inventory["Nails"]["quantity"] = inventory["Nails"]["quantity"] - int(row[2])
                    inventory["Screws"]["quantity"] = inventory["Screws"]["quantity"] - int(row[3])
                    inventory["Hammer"]["quantity"] = inventory["Hammer"]["quantity"] - int(row[4])
                    inventory["Electric Drill"]["quantity"] = inventory["Electric Drill"]["quantity"] - int(row[5])
                elif "S" in ID.get():
                    inventory["Nails"]["quantity"] = inventory["Nails"]["quantity"] + int(row[2])
                    inventory["Screws"]["quantity"] = inventory["Screws"]["quantity"] + int(row[3])
                    inventory["Hammer"]["quantity"] = inventory["Hammer"]["quantity"] + int(row[4])
                    inventory["Electric Drill"]["quantity"] = inventory["Electric Drill"]["quantity"] + int(row[5])
    
    with open('inventory.json', 'w') as file_handle:
        json.dump(inventory, file_handle)


def cancel_transaction():
    with open('transactions.csv', 'r', newline='') as inp, open('transactions_updated.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != ID.get():
                writer.writerow(row)

    update_inventory()
  
    messagebox.showinfo(title="Cancel Order", message=f"Transaction {ID.get()} has been canceled")
    clear_inputs()

    cancel_frame.grid_forget()
    option_frame.grid(row=2, column=0, padx=10, pady=10)

    update()


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

# pass_frame for empID/password input
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

quantity_nails = IntVar()
amount_sale_combobox_nails = ttk.Combobox(box3, textvariable=quantity_nails, values=numbers, state="readonly")
amount_sale_combobox_nails.grid(column=0, row=1, padx=5, pady=5)

quantity_screws = IntVar()
amount_sale_combobox_screws = ttk.Combobox(box3, textvariable=quantity_screws, values=numbers, state="readonly")
amount_sale_combobox_screws.grid(column=0, row=2, padx=5, pady=5)

quantity_hammer = IntVar()
amount_sale_combobox_hammer = ttk.Combobox(box3, textvariable=quantity_hammer, values=numbers, state="readonly")
amount_sale_combobox_hammer.grid(column=0, row=3, padx=5, pady=5)

quantity_electric_drill = IntVar()
amount_sale_combobox_electric_drill = ttk.Combobox(box3, textvariable=quantity_electric_drill, values=numbers, state="readonly")
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

file_handle = open("inventory.json")
inventory = json.load(file_handle)
file_handle.close()

sale_inventory_nails_label = Label(box3, text=f"{inventory['Nails']['quantity']}")
sale_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

sale_inventory_screws_label = Label(box3, text=f"{inventory['Screws']['quantity']}")
sale_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

sale_inventory_hammer_label = Label(box3, text=f"{inventory['Hammer']['quantity']}")
sale_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

sale_inventory_elecric_drill_label = Label(box3, text=f"{inventory['Electric Drill']['quantity']}")
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


amount_order_combobox_nails = ttk.Combobox(box4, textvariable=quantity_nails, values=numbers, state="readonly")
amount_order_combobox_nails.grid(column=0, row=1, padx=5, pady=5)


amount_order_combobox_screws = ttk.Combobox(box4, textvariable=quantity_screws, values=numbers, state="readonly")
amount_order_combobox_screws.grid(column=0, row=2, padx=5, pady=5)


amount_order_combobox_hammer = ttk.Combobox(box4, textvariable=quantity_hammer, values=numbers, state="readonly")
amount_order_combobox_hammer.grid(column=0, row=3, padx=5, pady=5)


amount_order_combobox_electric_drill = ttk.Combobox(box4, textvariable=quantity_electric_drill, values=numbers, state="readonly")
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

order_inventory_nails_label = Label(box4, text=f"{inventory['Nails']['quantity']}")
order_inventory_nails_label.grid(column=2, row=1, padx=5, pady=5)

order_inventory_screws_label = Label(box4, text=f"{inventory['Screws']['quantity']}")
order_inventory_screws_label.grid(column=2, row=2, padx=5, pady=5)

order_inventory_hammer_label = Label(box4, text=f"{inventory['Hammer']['quantity']}")
order_inventory_hammer_label.grid(column=2, row=3, padx=5, pady=5)

order_inventory_elecric_drill_label = Label(box4, text=f"{inventory['Electric Drill']['quantity']}")
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

cancel_button = Button(box5, command=cancel_transaction, text="Cancel Order")
cancel_button.grid(column=1, row=1, padx=5, pady=5)

# back button
order_back_button = Button(box5, command=back_to_option_from_cancel, text="Back")
order_back_button.grid(column=0, row=1, padx=5, pady=5)


win.mainloop()
