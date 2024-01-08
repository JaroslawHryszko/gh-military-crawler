import urllib.parse


class GithubSearchQueryBuilder:
    def __init__(self):
        self.text = ""
        self.languages = []

    def search_text(self, search_text: str) -> "GithubSearchQueryBuilder":
        # self.text += urllib.parse.quote(search_text)
        self.text += f"\"{(search_text.strip())}\""
        # self.text += search_text.strip()
        return self

    def set_languages(self, *languages) -> "GithubSearchQueryBuilder":
        # self.languages.extend(map(lambda x: urllib.parse.quote(x), languages))
        self.languages.extend(languages)
        return self

    def build(self) -> str:
        languages_str = list(map(lambda x: f"language:{x}", self.languages))
        # text_str = self.text + "+"
        return self.text + " " + " ".join(languages_str)


# TODO add github wrapper class
class GithubWrapper:
    def __init__(self, github_token: str, query_builder: GithubSearchQueryBuilder):
        self.query_builder = query_builder
        self.g = GitHub(token=github_token if github_token else "")

    def search_repositories(self, query: str):
        u = 0
        for repo_search_result in self.g.search_repositories(query=query, ):
            short_repository: ShortRepository = repo_search_result.repository
            short_user: ShortUser = short_repository.owner
            repository: Repository = self.g.repository(
                owner=short_user.login, repository=short_repository.name
            )
            user: User = self.g.user(short_user.login)
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
            print(repository.url)
            u += 1
            if u == 10:
                break
