import os
import time

import langdetect
import pytesseract
from github import Github, Auth
from github.Repository import Repository
from langdetect import detect
from PIL import Image
from dotenv import load_dotenv

from builder import GithubSearchQueryBuilder


def setup():
    load_dotenv(dotenv_path="../.env")
    pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_EXECUTABLE_PATH")


def read_military_names():
    with open("../data/military_names.txt", "r", encoding="utf-8") as file:
        military_names = file.read().split("\n")
    return military_names


def get_file_extension(file_name: str):
    parts = file_name.split('.')
    # Check if the file name starts with a dot or if there's only one part (no extension)
    if file_name.startswith('.') or len(parts) == 1:
        return None  # Return None for files like .gitignore or files without extensions
    else:
        return parts[-1]  # Return the last part as the file extension

# if in invalid extensions check only filename
invalid_extensions = [".dll", ".exe", ""]
def check_repo_contents(repo: Repository):
    contents = repo.get_contents("/")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            # TODO do the checking here
            print(file_content.decoded_content)
            (file_content.name)
            decoded = file_content.decoded_content.decode("utf-8")
            # print(decoded)
            # print(langdetect.detect(file_content.decoded_content))
            print(langdetect.detect(decoded))
            time.sleep(1)
    # check repositories with only txt files or images - leaked files


def main():
    # todo refactor this jeez it's awful
    setup()
    g = Github(auth=Auth.Token(os.getenv("GITHUB_TOKEN")))
    # TODO check if not getting rate limited without token
    # without token can't search for code
    # g = GitHub()

    military_names = read_military_names()
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
            check_repo_contents(code.repository)
            # print(code.repository)
        time.sleep(1)


if __name__ == "__main__":
    main()

    #
    # # Test file names
    # file_names = ['example.txt', '.gitignore', 'image.png', 'script.py', 'no_extension']
    #
    # # Get file extensions avoiding files starting with dot
    # valid_file_extensions = [get_file_extension(name) for name in file_names if not name.startswith('.')]
    #
    # print(valid_file_extensions)  # Print the valid file extensions