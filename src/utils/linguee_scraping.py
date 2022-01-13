"""This module provides functions to get words translations

functions
---------


"""
from bs4 import BeautifulSoup
import requests


def get_translation(word, languages):
    """scrape the different translations of a word
    given translation languages

    Parameters
    ----------
    word: str
        word to translate
    languages: str
        translatinng languages
        Ex: "anglais-français"

    Returns
    -------
    list
        list of the translations
    """
    # build url given word and languages
    url = build_url(word, languages)

    # get html source code
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    # find translations zone on web page
    div = soup.find("div", class_="translation_lines")

    # find all translations and store them in a list
    l_translations = []
    trad_zones = div.find_all("a", class_="dictLink featured")

    for t in trad_zones:
        l_translations.append(t.text)

    if not l_translations:
        l_translations.append("no translation available")

    return l_translations


def build_url(word, languages):
    """
    build url from linguee website given a word translating
    languages


    Parameters
    ----------
    word: str
        word to translate
    languages: str
        translatinng languages
        Ex: "anglais-français"

    Returns
    -------
    str:
        built url
    """
    print("https://www.linguee.fr/" + languages + "/search?source=auto&query=" + word.replace(" ", "+"))
    return "https://www.linguee.fr/" + languages + "/search?source=auto&query=" + word.replace(" ", "+")
