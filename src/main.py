import os
import time
import re
import unicodedata
from typing import List, Set

import langdetect
import pytesseract
from dotenv import load_dotenv
from github import Auth, Github
from github.ContentFile import ContentFile
from github.Repository import Repository
from PIL import Image

from builder import GithubSearchQueryBuilder


def setup():
    load_dotenv(dotenv_path="../.env")
    pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_EXECUTABLE_PATH")


def read_keywords():
    military_names = []
    with open("../data/military_names.txt", "r", encoding="utf-8") as file:
        military_names.extend(file.read().split("\n"))
    with open("../data/other.txt", "r", encoding="utf-8") as file:
        military_names.extend(file.read().split("\n"))
    return military_names




def get_file_extension(file_name: str):
    parts = file_name.split('.')
    # Check if the file name starts with a dot or if there's only one part (no extension)
    if file_name.startswith('.') or len(parts) == 1:
        return None  # Return None for files like .gitignore or files without extensions
    else:
        return parts[-1]  # Return the last part as the file extension


# if in invalid extensions check only filename
invalid_extensions: Set[str] = {".dll", ".exe"}
cyryllic_languages: Set[str] = {'be', 'bg', 'kk', 'ky', 'mk', 'sr', 'ru', 'tg', 'tk', 'uk', 'uz'}


def is_cyrillic(char):
    return 'CYRILLIC' in unicodedata.name(char, '')


def handle_pdf_file():
    pass


def check_file_contents(file_content: ContentFile) -> int:
    """

    :param file_content:
    :return: probability of a repository
    """
    probability = 0
    extension = get_file_extension(file_content.name)
    # check filename
    if "ru" in map(lambda x: x.lang, langdetect.detect_langs(file_content.name)):
        probability += 1

    if extension in invalid_extensions:
        return
    elif extension == ".pdf":
        probability += handle_pdf_file()

    decoded_file_contents = file_content.decoded_content.decode("utf-8")

    # based on probability - can get different results each time
    # TODO langdetect doesn't recognise russian words not written in Cyrillic
    range_probablility = 0
    range_cap = 10
    for _ in range(range_cap):
        if "ru" in map(lambda x: x.lang, langdetect.detect_langs(decoded_file_contents)):
            range_probablility += 1

    probability += int(range_probablility / range_cap)

    # get all file contents as single words, then detect what language are they
    # words_in_file = re.split(r"\s", file_content.decoded_content.decode("utf-8"))
    # TODO check every single word?

    return probability


def check_repo_contents(repo: Repository):
    contents = repo.get_contents("/")
    while contents:
        file_contents = contents.pop(0)
        if file_contents.type == "dir":
            contents.extend(repo.get_contents(file_contents.path))
        else:
            check_file_contents(file_contents)
            # TODO do the checking here
        time.sleep(1)
    # TODO what about images?


def main():
    # todo refactor this jeez it's awful
    setup()
    g = Github(auth=Auth.Token(os.getenv("GITHUB_TOKEN")))
    # TODO check if not getting rate limited without token
    # without token can't search for code
    # g = GitHub()

    military_names: List[str] = read_keywords()
    possible_matches: List[Repository] = []
    # i = 1
    for name in military_names:
        # print(f"{i}. {name}")
        # i += 1
        query = GithubSearchQueryBuilder()\
            .search_text(search_text=name)\
            .set_languages("Assembly", "Ada", "C++", "C", "Rust")\
            .build()

        codes = g.search_code(query=query)
        for code in codes:
            if check_repo_contents(code.repository):
                possible_matches.append(code.repository)
            # TODO check user
            # check_user(...)
        time.sleep(1)


if __name__ == "__main__":
    main()
