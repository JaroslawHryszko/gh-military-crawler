from pprint import pprint

from github3 import GitHub
from github3.repos import ShortRepository, Repository
from github3.users import ShortUser, User

from langdetect import detect

from builder import QueryBuilder
from PIL import Image

import pytesseract


def setup():
    with open('../.env') as file:
        path_to_tesseract = file.read().strip()
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

# TODO add poetry, pylint, isort, black

words = ['military', 'war', '']

def main():
    g = GitHub()
    query = QueryBuilder().search_text(search_text="tet ris").language("Assembly").build()
    # loop with all the keywords here

    # check repositories with only txt files or images - leaked files

    u = 0
    for repo_search_result in g.search_repositories(query=query):
        short_repository: ShortRepository = repo_search_result.repository
        short_user: ShortUser = short_repository.owner
        repository: Repository = g.repository(owner=short_user.login, repository=short_repository.name)
        user: User = g.user(short_user.login)
        # check if name is in russian
        # check if files have russian
        # check stars
        # check followers/following
        # created after the beginning of the war
        # probably has no homepage url


        # check titles for keywords, like army etc.
        #
        print(short_user)
        print(user)
        u += 1
        if u == 10:
            break


if __name__ == "__main__":
    # main()
    # import wikipediaapi
    # wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    # page = wiki_wiki.page("List of active Russian Air Force aircraft")
    import requests
    page = requests.get('https://en.wikipedia.org/wiki/List_of_active_Russian_Air_Force_aircraft')
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(page.content, 'html.parser')
    # table = soup.find(attrs={"class": "wikitable"})
    # table has 6 columns, the first one is the name of the aircraft
    table = list(map(lambda x: x.text, soup.find(class_="wikitable").find_all("td")[0::6]))
    pprint(table)
    page = requests.get('https://en.wikipedia.org/wiki/List_of_active_Russian_military_aircraft')
    # wikitable sortable    jquery - tablesorter
    # wikitable do skipa, samemu pobrac
    pass