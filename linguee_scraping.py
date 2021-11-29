from bs4 import BeautifulSoup
import requests


def build_url(mot, langue):
    # return "https://www.linguee.fr/" + langue + "/traduction/" + mot + ".html"
    return "https://www.linguee.fr/" + langue + "/search?source=auto&query=" + mot.replace(" ", "+")


def get_trad(mot, langue):
    url = build_url(mot, langue)
    # print(requests.get(url))
    #print(url)
    html_text = requests.get(url).text

    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')

    div = soup.find("div", class_="translation_lines")

    trad_zones = div.find_all("a", class_="dictLink featured")

    l_trad = []
    for t in trad_zones:
        l_trad.append(t.text)

    return l_trad


# print(get_trad(trad_mot, trad_langue))

""""
with open('page_test.html', 'r') as html_file:

    html_text = html_file.read()

    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')

    div = soup.find("div", class_="translation_lines")

    a_s = div.find_all("a", class_="dictLink featured")

    l_trad = []
    for a in a_s:
        l_trad.append(a.text)

    print(l_trad)"""
