from os import write
from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # messagebox.showinfo(title="title", message="message")

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} '
                                        f'\nPassword: {password} \nIs it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

    

        



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Gui")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)



#Labels
web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "gmail.com")

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, columnspan=1)




Gen_password_btn = Button(text="Generate Password")
Gen_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)



window.mainloop()