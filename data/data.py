import re

import requests
from bs4 import BeautifulSoup


def scrap_wikipedia_page_table(wikipedia_link: str):
    page = requests.get(wikipedia_link)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    first_column_values = []
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            columns = row.find_all("td")
            if columns:
                # regex for asdf^[1]
                first_column_value = re.sub(
                    r"\[.*]", "", columns[0].search_text.strip()
                )
                first_column_values.append(first_column_value)
    return first_column_values


if __name__ == "__main__":
    links = [
        "https://en.wikipedia.org/wiki/List_of_active_Russian_Air_Force_aircraft",
        "https://en.wikipedia.org/wiki/List_of_active_Russian_military_aircraft",
        "https://en.wikipedia.org/wiki/List_of_equipment_of_the_Russian_Ground_Forces",
    ]
    formatted_names = []
    for link in links:
        formatted_names.extend(scrap_wikipedia_page_table(link))
    formatted_names = set(filter(lambda x: x.strip(), formatted_names))
    with open("military_names.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(formatted_names))
