import time
from typing import List, Tuple

import langdetect
from github import Auth, Github, Repository, NamedUser
from github.ContentFile import ContentFile

from constants import image_extensions, invalid_extensions, MIN_PROBABILITY_TO_ACCEPT
from utils import check_for_russian, get_file_extension, handle_pdf_file, handle_image_file


class GithubSearchQueryBuilder:
    def __init__(self):
        self.search_text = ""
        self.languages = []

    def set_search_text(self, search_text: str) -> "GithubSearchQueryBuilder":
        self.search_text += f'"{(search_text.strip())}"'
        return self

    def set_languages(self, *languages) -> "GithubSearchQueryBuilder":
        self.languages.extend(languages)
        return self

    def build(self) -> str:
        languages_str = list(map(lambda x: f"language:{x}", self.languages))
        # TODO change that into something nicer
        return self.search_text + " " + " ".join(languages_str)


caught_invalid_extensions = []

class GithubWrapper:
    def __init__(self, github_token: str, query_builder: GithubSearchQueryBuilder):
        self.query_builder: GithubSearchQueryBuilder = query_builder
        self.g = Github(auth=Auth.Token(github_token))

    def check_all(self):
        pass

    def check_repositories(self, query: str) -> List[Repository]:
        possible_matches = []
        repositories = self.g.search_repositories(query=query)
        for repo_search_result in repositories:
            # check if name is in russian
            # check if files have russian
            # check stars
            # check followers/following
            # created after the beginning of the war
            # probably has no homepage url

            # check titles for keywords, like army etc.
            repo_score = 0
            if self._check_repo_contents(repo_search_result):
                repo_score += 0.5
            # TODO check user
            if self._check_user(repo_search_result.owner):
                repo_score += 0.5
            if repo_score >= 0.5:
                possible_matches.append(repo_search_result)
        time.sleep(1)
        return possible_matches

    def check_code(self, query: str) -> List[Repository]:
        possible_matches = []
        codes = self.g.search_code(query=query)
        for code_search_result in codes:
            repo_score = 0
            if self._check_repo_contents(code_search_result.repository):
                repo_score += 0.5
            # TODO check user
            if self._check_user(code_search_result.repository.owner):
                repo_score += 0.5
            if repo_score >= 0.5:
                possible_matches.append(code_search_result.repository)
        time.sleep(1)
        return possible_matches

    def _check_repo_contents(self, repo: Repository):
        contents: List[ContentFile] = repo.get_contents("/")
        processed_files = []
        number_of_files = 0
        while contents:
            file_contents = contents.pop(0)
            if file_contents.type == "dir":
                contents.extend(repo.get_contents(file_contents.path))
            else:
                number_of_files += 1
                processed_files.append(self._check_file_contents(file_contents))
            time.sleep(1)

        # TODO move to constants
        lower_bound = int(0.1 * number_of_files)
        valid_files = 0
        for (probability, _) in processed_files:
            if probability > MIN_PROBABILITY_TO_ACCEPT:
                valid_files += 1
                if valid_files >= lower_bound:
                    break

        return valid_files >= lower_bound

    # TODO consider moving to file checking class (with handle_pdf_file function)
    # TODO change return type to something else
    def _check_file_contents(self, file_content: ContentFile) -> (float, bool):
        """

        :param file_content:
        :return: tuple (probability, if filename is in russian)
        """
        probability = 0.0
        extension = get_file_extension(file_content.name)
        # TODO use has_russian_filename or refactor it
        has_russian_filename = bool(check_for_russian(file_content.name))

        # TODO detect extension using mimetypes
        if extension in invalid_extensions:
            return probability, has_russian_filename
        elif extension == ".pdf":
            return handle_pdf_file(file_content), has_russian_filename
        elif extension in image_extensions:
            return handle_image_file(file_content), has_russian_filename

        try:
            decoded_file_contents = file_content.decoded_content.decode("utf-8")
        except UnicodeDecodeError:
            print(f"Invalid extension: {extension}")
            caught_invalid_extensions.append(extension)
            return 0, has_russian_filename

        # based on probability - can get different results each time
        # TODO langdetect doesn't recognise russian words not written in Cyrillic
        #  check if setting the seed changes anything
        range_probability = 0.0
        range_cap = 10
        for _ in range(range_cap):
            range_probability += check_for_russian(decoded_file_contents)

        probability += range_probability / range_cap

        # TODO check every single word?
        # get all file contents as single words, then detect what language are they
        # words_in_file = re.split(r"\s", file_content.decoded_content.decode("utf-8"))

        return probability, has_russian_filename

    def _check_user(self, user: NamedUser):
        pass
