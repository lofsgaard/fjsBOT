import requests


def classes_eq():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/classes_eq.txt'
    page = requests.get(url)
    return page.text


def classes_noggen():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/classes_noggen.txt'
    page = requests.get(url)
    return page.text


def classes_of():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/classes_of.txt'
    page = requests.get(url)
    return page.text


def classes_savant():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/classes_savant.txt'
    page = requests.get(url)
    return page.text


def raid_tider():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/raid_tider.txt'
    page = requests.get(url)
    return page.text


def about():
    url = 'https://raw.githubusercontent.com/Terudo/rabiat-shit/main/rekruttering/about.txt'
    page = requests.get(url)
    return page.text


if __name__ == "__main__":
    print(classes_eq())
    print(classes_noggen())
    print(classes_of())
    print(classes_savant())
    print(raid_tider())

