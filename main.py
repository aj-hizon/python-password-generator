from tkinter import *
from tkinter import messagebox

#---------------------------- PASSWORD GENERATOR ---------------------------#
 
 



#---------------------------- SAVE PASSWORD ---------------------------#
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get() 

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.askretrycancel(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?:")
            
        with open(r"C:\Users\Hizon\Desktop\Coding\python\day-29-password-manager-gui\data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}")
  

#---------------------------- UI SETUP ---------------------------#

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
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=4, column=1, columnspan=1)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop() 
