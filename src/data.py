import requests

from bs4 import BeautifulSoup

# def scrap_wikipedia_military_data():
#     page = requests.get(
#         "https://en.wikipedia.org/wiki/List_of_active_Russian_Air_Force_aircraft"
#     )
#
#     soup = BeautifulSoup(page.content, "html.parser")
#     # table has 6 columns, the first one is the name of the aircraft
#     first_link_tables = list(map(lambda x: x.text, soup.find(class_="wikitable").find_all("td")[0::6]))
#
#     ###
#
#     page = requests.get(
#         "https://en.wikipedia.org/wiki/List_of_active_Russian_military_aircraft"
#     )
#     soup = BeautifulSoup(page.content, "html.parser")
#     # tabs we're interested in have class="wikitable sortable jquery-tablesorter", but searching for it does not work
#     # they have 8 columns, the one with less has been manually scraped in data/aircraft.txt
#     asdf = soup.find_all(class_="sortable")
#     # print(asdf)
#     second_link_tables = [item for table in list(map(lambda x: x.find_all("td"), soup.find_all(class_="sortable"))) for item in table][0::8]
#     second_link_tables = list(map(lambda x: x.text, second_link_tables))
#     # wikitable sortable    jquery - tablesorter
#     # wikitable do skipa, samemu pobrac
#     # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
#     page = requests.get(
#         "https://en.wikipedia.org/wiki/List_of_equipment_of_the_Russian_Ground_Forces"
#     )
#     soup = BeautifulSoup(page.content, "html.parser")
#
#     # https://commonslibrary.parliament.uk/research-briefings/cbp-9477/
#     # to sprawdzic
#     pass


def scrap_wikipedia_page_table(wikipedia_link: str):
    page = requests.get(wikipedia_link)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all(class_="wikitable")
    # TODO do it better lol
    # investigated it with debugger, .contents[1] gets the table content (without <table>)
    # .contents[0] gets the first row (with column names)
    # count <th> - that's how many columns are there, first one is name
    tables = list(zip(tables, list(map(lambda table: str(table.contents[1].contents[0]).count("th"), tables))))
    formatted_names = []
    for table, columns in tables:
        rows = list(map(lambda row: row.text, table.find_all("td")))
        formatted_names.extend(rows[0::columns])
    return formatted_names


if __name__ == "__main__":
    links = [
        "https://en.wikipedia.org/wiki/List_of_active_Russian_Air_Force_aircraft",
        "https://en.wikipedia.org/wiki/List_of_active_Russian_military_aircraft",
        "https://en.wikipedia.org/wiki/List_of_equipment_of_the_Russian_Ground_Forces",
    ]
    formatted_names = []
    for link in links:
        formatted_names.extend(scrap_wikipedia_page_table(link))
    formatted_names = set(formatted_names)
    pass
    # with open("../data/military_names.txt", "w") as file:
    #     file.write(formatted_names)
