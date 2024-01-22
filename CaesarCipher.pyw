# Name: Noelle Dacayo
# Date: December 5th, 2022
# App Name: Caesar Cipher
# Description: App that will encrypt and decrypt the user's message

# hi hi (^^ )/

# Imports
from tkinter import * # Import the tkinter module
from tkinter.ttk import * # Replaces the W95 look with a modern one
from tkinter import messagebox # Pop-up message



# CONSTANTS
OPTIONS = ("Encrypt", "Decrypt")
ENCRYPTION_KEY = 1025  # Increments to plus or minus from the ascii table


# Defining functions
# ------------------------------------------------------------------------------------------------------------------------------------
# Allows the user to user to use [Enter] instead of pressing the Confess button and allows the user to use [ESC] to clear the window
def key_handler(event:Event):
    """
    Handles key press
    """
    if event.keysym == "Return": # R is uppercase - enter key
        go_click()
    elif event.keysym == "Escape": # Esc key
        clear_click()

# ------------------------------------------------------------------------------------------------------------------------------------
# Defining what the clear button will do when clicked
def clear_click():
    """
    Dirty deletes your dirty confession
    """
    options_selection.set("Confess or Hide?")
    input_text.set("")
    output_text.set("")

# ------------------------------------------------------------------------------------------------------------------------------------
# Encrypts user inputted plain text
def encrypt(message):
    """
    Encrypts your confession by shifting the key-code by 2
    """
    encrypted = ""
    for letter in message:
        encrypted += chr(ord(letter) + ENCRYPTION_KEY)
    return encrypted

# ------------------------------------------------------------------------------------------------------------------------------------
# Decrypts an encrypted message. It doesn't work for plain text when the encryption key is too high, Colin found that out and I'm equally as annoyed by it TT
def decrypt(message):
    """
    Reveals your dirty confession for the world to see
    """
    decrypted = ("")
    for letter in message:
        decrypted += chr(ord(letter) - ENCRYPTION_KEY)
    return decrypted

# ------------------------------------------------------------------------------------------------------------------------------------
# Defines what the [CONFESS] button does. Shows an error when nothing is in the input box
def go_click():
    """
    Encrypts or decrypts your dirty confession
    """
    if input_text.get() == "":
        messagebox.showerror(title="Error!", message="Don't lie to me. \nI know you have something to confess.")

    if options_selection.get() == OPTIONS[0]:
        output_text.set(encrypt(input_entry.get()))
    elif options_selection.get() == OPTIONS[1]:
        output_text.set(decrypt(input_entry.get()))





# Set up the window
# ------------------------------------------------------------------------------------------------------------------------------------
# Create a window
window = Tk()                                       # Create a window
window.title("Caesar Cipher - Noelle Dacayo")       # Changes the title
window.iconbitmap("salad.ico")                      # Changes the window's icon. I know it's not the salad but I thought it was funny lol
window.resizable(width=False, height=False)         # Not resizable
window.bind("<Key>", key_handler)                   # Allows key presses
window.configure(bg='#661321')                      # Changes the colour of the window background

# ------------------------------------------------------------------------------------------------------------------------------------
# Create a frame - Will hold all the other widgets
input_frame = Frame(borderwidth=10)
output_frame = Frame(borderwidth=7)

# ------------------------------------------------------------------------------------------------------------------------------------
# Input
input_label = Label(input_frame, text="Do you have a secret to confess? ", width=55)
input_text = Variable()
input_entry = Entry(input_frame, width=55, textvariable=input_text)

# ------------------------------------------------------------------------------------------------------------------------------------
# Dropdown
options_selection = Variable() 
options_selection.set("Confess or Hide")
options_combobox = Combobox(input_frame, values=OPTIONS, width=35, textvariable=options_selection, state="readonly")

# ------------------------------------------------------------------------------------------------------------------------------------
# Button
go_button = Button(input_frame, text="C O N F E S S", width=15, command=go_click)
clear_button = Button(output_frame, text="You Have Been Forgiven", command=clear_click)

# ------------------------------------------------------------------------------------------------------------------------------------
# Output
output_text = Variable()
output_label = Label(output_frame, text="Secret Confession")
output_entry = Entry(output_frame, font="Gothic 17",justify=CENTER, state="readonly", textvariable=output_text, width=35)





# Pack pack pack pack pack
# ------------------------------------------------------------------------------------------------------------------------------------
# Input packing
input_frame.pack(padx=10,pady=10)
input_label.pack(anchor="w")
input_entry.pack(anchor="w")
go_button.pack(pady=(5,0), side="right")
options_combobox.pack(pady=(5,0), side="left")
# ------------------------------------------------------------------------------------------------------------------------------------
# Output packing
output_frame.pack(padx=10, pady=(50,10))
output_label.pack(anchor="w")
output_entry.pack(pady=(0,5))
clear_button.pack(pady=(5,5))
# ------------------------------------------------------------------------------------------------------------------------------------



# Make the window visible
window.mainloop()


# bye byeee (^^ )/
# This was a pretty fun project to do, I had a good time experimenting with the output and the GUI