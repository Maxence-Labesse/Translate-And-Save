from bs4 import BeautifulSoup
import requests


def get_translation(word, language):
    """
    scrape the different translations for a word to translate and a language

    Parameters
    ----------
    word (string): word to translate
    language (string) : translation language

    Returns
    -------
    (list): list of translations for the word
    """
    # build urm according to word and language
    url = build_url(word, language)

    # get html source code
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    # find translations zone on web page
    div = soup.find("div", class_="translation_lines")

    # find all translations and store them in a list
    trad_zones = div.find_all("a", class_="dictLink featured")
    l_trad = []
    for t in trad_zones:
        l_trad.append(t.text)

    return l_trad


def build_url(word, language):
    """
    build url from linguee website for a word to translate and a language

    Parameters
    ----------
    word (string): word to translate
    language (string) : translation language

    Returns
    -------
    (string): built url
    """
    # return "https://www.linguee.fr/" + langue + "/traduction/" + mot + ".html"
    return "https://www.linguee.fr/" + language + "/search?source=auto&query=" + word.replace(" ", "+")
