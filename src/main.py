import os

import pytesseract
from dotenv import load_dotenv

from github_wrapper import GithubSearchQueryBuilder, GithubWrapper
from src.constants import programming_languages, ROOT_PROJECT_PATH
from src.utils import read_keywords


def setup():
    load_dotenv(dotenv_path=ROOT_PROJECT_PATH / ".env")
    tesseract_executable_path = os.getenv("TESSERACT_EXECUTABLE_PATH")
    if tesseract_executable_path is not None:
        pytesseract.pytesseract.tesseract_cmd = tesseract_executable_path


def main():
    # todo refactor setup()
    setup()
    g = GithubWrapper(
        github_token=os.getenv("GITHUB_TOKEN"), query_builder=GithubSearchQueryBuilder()
    )

    military_names = read_keywords()
    for name in military_names:
        query = (
            GithubSearchQueryBuilder()
            .set_search_text(search_text=name)
            .set_languages(*programming_languages)
            .build()
        )
        g.check_code(query)
        g.check_repositories(query)


if __name__ == "__main__":
    main()
