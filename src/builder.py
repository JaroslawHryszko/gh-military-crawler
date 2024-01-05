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
