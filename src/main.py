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
    repositories = []
    for name in military_names:
        query = (
            GithubSearchQueryBuilder()
            .set_search_text(search_text=name)
            .set_languages(*programming_languages)
            .build()
        )
        print(f"Searching for query: {query}\n")
        repositories.extend(g.check_code(query))
        repositories.extend(g.check_repositories(query))

    print(repositories)


if __name__ == "__main__":
    main()
    from github_wrapper import caught_invalid_extensions
    print(caught_invalid_extensions)
