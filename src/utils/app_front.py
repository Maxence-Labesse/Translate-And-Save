""" This module provides functions to build the app interface

function
--------
open_app:
    open app interface
submit_translation:
    get translations when button is pressed
"""
from tkinter import *
import tkinter.ttk as ttk
from datetime import date
from src.utils.linguee_scraping import get_translation

# initiate list to save translations in .txt file and translation
# row in the file
translations_to_save_in_txt = []
translation_row = 2


def open_app():
    """build app interface

    this window contains a textfield for the word to translate,
    a dropdown menu for the translating languages and a submit
    button

    Returns
    -------
    root: tkinter.Tk
        built app
    """
    # Window global settings
    root = Tk()
    root.title("Traducteur")
    style = ttk.Style()
    style.theme_use('clam')
    # root.geometry('300x120')

    global Save_button

    # init save button which will appear after first translation
    Save_button = Button(root, text="")

    # Entry for word to translate
    word_entry = Entry(root)
    word_entry.grid(row=0, column=0, ipadx=20, padx=10, pady=(10, 0))

    # languages options and dropdown
    options = ["francais-anglais", "anglais-francais"]
    selected_languages = StringVar()
    selected_languages.set("anglais-francais")
    drop = OptionMenu(root, selected_languages, *options)
    drop.grid(row=0, column=1, padx=10, pady=(10, 0))

    # submit button
    mybutton = Button(root, text="Get translation",
                      command=lambda: submit_translation(root, word_entry, selected_languages))
    mybutton.grid(row=1, columnspan=2, padx=10, pady=10, ipadx=90)

    return root


def submit_translation(root, word, languages):
    """when "Get translation" button is pressed, scrape linguee.fr website
    to get translation for a given word and translating languages

    After first translation, make "save button" appear on root

    Parameters
    ----------
    root: tkinter.Tk
        app main window
    word:
        word to translate from textfield
    languages:
        translatinng languages from dropdown menu
        Ex: "anglais-français"
    """
    global translation_row
    global Save_button

    # get translation(s) for word and languages
    l_translations = get_translation(word.get(), languages.get())

    # display translations
    translation_label = word.get() + " -> " + l_translations[0]
    if len(l_translations) > 1:
        for t in l_translations[1:]:
            translation_label += " / " + t

    label = Label(root, text=translation_label)
    label.grid(row=translation_row, columnspan=2)

    # add translations to list that will be exported into text.file
    translations_to_save_in_txt.append(translation_label)

    # create a button to close and save the app
    Save_button.destroy()
    Save_button = Button(root, text="Save and exit", command=lambda: save_quit(root))
    Save_button.grid(row=translation_row + 1, columnspan=2, pady=10, padx=10, ipadx=50)

    translation_row += 1


def save_quit(root):
    """Save translations into a .txt file when "save and exit"
    button is pressed.

    Close the app

    Parameters
    ----------
    root: tkinter.Tk
        app main window
    """
    # Save translations
    with open("Traductions_" + date.today().strftime("%d-%b-%Y") + ".txt", "w") as f:
        for trad in translations_to_save_in_txt:
            f.write(trad + '\n')
    # close app
    root.destroy()
