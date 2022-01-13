from tkinter import *
import tkinter.ttk as ttk
from linguee_scraping import *
from datetime import date

# initiate list to save translations in .txt file and translation number
l_export_trad = []
translation_row = 2


def submit():
    """
    when "obtenir la traduction" button is pressed, scrape translations on linguee for the word and language filled by
    the user
    """
    global translation_row
    global Save_button

    # get translation(s) for word and language
    l_traductions = get_translation(e.get(), var.get())

    # word -> translations layout
    label_trad = e.get() + " -> " + l_traductions[0]
    if len(l_traductions) > 1:
        for t in l_traductions[1:]:
            label_trad += " / " + t
    # add word and translations to list
    l_export_trad.append(label_trad)

    # display translations
    myLabel = Label(root, text=label_trad)
    myLabel.grid(row=translation_row, columnspan=2)

    # create a button to close and save the app
    Save_button.destroy()
    Save_button = Button(root, text="Sauvegarder et fermer", command=save_quit)
    Save_button.grid(row=translation_row + 1, columnspan=2, pady=10, padx=10, ipadx=50)

    translation_row += 1


def save_quit():
    """
    When "Sauvegarder et fermer" button is pressed, save translations in a .txt file and close the app
    """
    # Save translations
    with open("Traductions_" + date.today().strftime("%d-%b-%Y") + ".txt", "w") as f:
        for trad in l_export_trad:
            f.write(trad + '\n')
    # close app
    root.destroy()


# Window global settings
root = Tk()
root.title("Traducteur")
style = ttk.Style()
style.theme_use('clam')
# root.geometry('300x120')

# init save button which will appear after first translation
Save_button = Button(root, text="")

# Entry for word to translate
e = Entry(root)
e.grid(row=0, column=0, ipadx=20, padx=10, pady=(10, 0))

# language options
options = ["francais-anglais", "anglais-francais"]
var = StringVar()
var.set("anglais-francais")
# language dropdown
drop = OptionMenu(root, var, *options)
drop.grid(row=0, column=1, padx=10, pady=(10, 0))

# submit and save button
myButton = Button(root, text="Obtenir la traduction", command=submit)
myButton.grid(row=1, columnspan=2, padx=10, pady=10, ipadx=90)

root.mainloop()
