from importlib.machinery import FileFinder
from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
import json 

#---------------------------- PASSWORD GENERATOR ---------------------------#
 
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for n in range(nr_letters)]
    password_list +=  [random.choice(symbols) for n in range(nr_symbols)]
    password_list += [random.choice(numbers) for n in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

#---------------------------- SAVE PASSWORD ---------------------------#

def save():

    website = website_entry.get()
    email = email_entry.get()              
    password = password_entry.get() 
    new_data = { 
        website: {
            "email": email,
            "password": password,
            } 
        }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.askretrycancel(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:  
        try:
            with open(r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open(r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)
            with open(r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
#---------------------------- FIND PASSWORD ---------------------------#

def find_password():  
    website = website_entry.get()
    try:
        with open(r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")      
        else: 
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


#----------------------------- UI SETUP -------------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx = 100, pady = 50, bg = "#FFFFFF")


canvas = Canvas(width = 200, height = 200, bg = "#FFFFFF",  highlightthickness = 0 )
lock_image = PhotoImage(file = r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", bg="#FFFFFF")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="#FFFFFF")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="#FFFFFF")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "2022308474@dhvsu.edu.ph")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, columnspan=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(row=3, column=2, columnspan=1)
add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, columnspan=1)

window.mainloop() 
