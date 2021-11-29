from tkinter import *
import tkinter.ttk as ttk
from linguee_scraping import *
from datetime import date

# First widget: global window
root = Tk()
root.title("Traducteur")
style = ttk.Style()
style.theme_use('clam')
# root.geometry('300x120')

e = Entry(root)
e.grid(row=0, column=0, ipadx=20, padx=10, pady=(10, 0))
options = ["francais-anglais", "anglais-francais"]
var = StringVar()
var.set("anglais-francais")
drop = OptionMenu(root, var, *options)
drop.grid(row=0, column=1, padx=10, pady=(10, 0))

i = 2

Save_button = Button(root, text="")

l_export_trad = []


def myClick():
    global i
    global Save_button

    l_traductions = get_trad(e.get(), var.get())

    label_trad = e.get() + " -> " + l_traductions[0]
    if len(l_traductions) > 1:
        for t in l_traductions[1:]:
            label_trad += " / " + t

    l_export_trad.append(label_trad)

    myLabel = Label(root, text=label_trad)
    myLabel.grid(row=i, columnspan=2)

    Save_button.destroy()
    Save_button = Button(root, text="Sauvegarder les traductions et fermer", command=save_quit)
    Save_button.grid(row=i + 1, columnspan=2, pady=10, padx=10, ipadx=50)
    i += 1


def save_quit():
    with open("Traductions_" + date.today().strftime("%d-%b-%Y") + ".txt", "w") as f:
        for trad in l_export_trad:
            f.write(trad + '\n')
    root.destroy()


myButton = Button(root, text="Obtenir la traduction", command=myClick)
myButton.grid(row=1, columnspan=2, padx=10, pady=10, ipadx=90)

root.mainloop()
