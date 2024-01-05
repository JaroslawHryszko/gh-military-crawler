from pprint import pprint

import pytesseract
from github3 import GitHub
from github3.repos import Repository, ShortRepository
from github3.users import ShortUser, User
from langdetect import detect
from PIL import Image

from builder import QueryBuilder


def setup():
    with open("../.env") as file:
        path_to_tesseract = file.read().strip()
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract


# TODO add poetry, pylint, isort, black

words = ["military", "war", ""]


def main():
    g = GitHub()
    query = (
        QueryBuilder().search_text(search_text="tet ris").language("Assembly").build()
    )
    # loop with all the keywords here

    # check repositories with only txt files or images - leaked files

    u = 0
    for repo_search_result in g.search_repositories(query=query):
        short_repository: ShortRepository = repo_search_result.repository
        short_user: ShortUser = short_repository.owner
        repository: Repository = g.repository(
            owner=short_user.login, repository=short_repository.name
        )
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
    main()
