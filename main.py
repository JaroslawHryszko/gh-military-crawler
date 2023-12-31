from github3 import login, GitHub


def read_gh_token() -> str:
    with open('.info', 'r') as token_file:
        token = token_file.read().strip()
    return token


class QueryBuilder:
    def __init__(self):
        self.text = ""
        self.languages = []

    def search_text(self, search_text: str) -> "QueryBuilder":
        self.text += search_text
        return self

    def language(self, language: str) -> "QueryBuilder":
        self.languages.append(language)
        return self

    def build(self) -> str:
        languages_str = list(map(lambda x: f"language:{x}", self.languages))
        text_str = self.text + "+"
        return text_str + "+".join(languages_str)

def main():
    g = GitHub()
    query = QueryBuilder().search_text(search_text="tetris").language("Assembly").build()
    print(query)
    # loop with all the keywords here
    print(g.search_repositories(query=f"tetris+language:Assembly"))


if __name__ == "__main__":
    main()
