import requests
from bs4 import BeautifulSoup
import re

# reading fandom webpage using beautiful soup

# soup = BeautifulSoup(requests.get('https://ageofempires.fandom.com/wiki/Technology_(Age_of_Empires_II)').content, 'lxml')
url = "https://ageofempires.fandom.com/api.php"

params = {
    "action": "parse",
    "page": "Technology_(Age_of_Empires_II)",
    "prop": "text",
    "format": "json",
}

headers = {"User-Agent": "Mozilla/5.0 (compatible; AoE2Bot/1.0)"}
request = requests.get(url, params=params, headers=headers)
data = request.json()["parse"]["text"]["*"]

soup = BeautifulSoup(data, "lxml")

with open("output.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

# finding required tables using their section IDs. The page contains other
# tables before the technology tables, so fixed indexes are not reliable.
def technology_table(section_id):
    return soup.find(id=section_id).find_next("table")


def technology_rows(table):
    headers = [
        cell.get_text(" ", strip=True).lower() for cell in table.find("tr").find_all(["th", "td"], recursive=False)
    ]
    columns = {name: headers.index(name) for name in ("technology", "cost", "effect", "time")}
    rows = []
    spans = {}

    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td", recursive=False)
        if not cells:
            continue

        expanded = []
        column = 0
        new_spans = {}
        for cell in cells:
            while column in spans:
                expanded.append(spans[column][0])
                column += 1
            text = cell.get_text(" ", strip=True)
            expanded.append(text)
            rowspan = int(cell.get("rowspan", 1))
            if rowspan > 1:
                new_spans[column] = (text, rowspan - 1)
            column += 1

        while column in spans:
            expanded.append(spans[column][0])
            column += 1

        spans = {
            span_column: (text, remaining - 1) for span_column, (text, remaining) in spans.items() if remaining > 1
        }
        spans.update(new_spans)
        rows.append({name: expanded[index] for name, index in columns.items()})

    return rows


section_ids = {
    "buildings": "Building_technologies",
    "eco": "Economy_technologies",
    "monastery": "Monastery_technologies",
    "infantry": "Infantry",
    "ranged": "Missile_/_siege",
    "cav": "Cavalry",
    "ship": "Naval_technologies",
    "misc": "Miscellaneous_technologies",
}
technology_data = {name: technology_rows(technology_table(section_id)) for name, section_id in section_ids.items()}

eco_text = technology_data["eco"]
buildings_text = technology_data["buildings"]
monastery_text = technology_data["monastery"]
infantry_text = technology_data["infantry"]
ranged_text = technology_data["ranged"]
cav_text = technology_data["cav"]
ship_text = technology_data["ship"]
misc_text = technology_data["misc"]


# declaring temporary variables for storing data fetched from tables
def table_values(table_data):
    return (
        [row["cost"] for row in table_data],
        [row["time"] for row in table_data],
        [row["effect"] for row in table_data],
        [row["technology"] for row in table_data],
    )


eco_cost, eco_time, eco_effect, eco_tech = table_values(eco_text)
buildings_cost, buildings_time, buildings_effect, buildings_tech = table_values(buildings_text)
monastery_cost, monastery_time, monastery_effect, monastery_tech = table_values(monastery_text)
infantry_cost, infantry_time, infantry_effect, infantry_tech = table_values(infantry_text)
ranged_cost, ranged_time, ranged_effect, ranged_tech = table_values(ranged_text)
cav_cost, cav_time, cav_effect, cav_tech = table_values(cav_text)
ship_cost, ship_time, ship_effect, ship_tech = table_values(ship_text)
misc_cost, misc_time, misc_effect, misc_tech = table_values(misc_text)

# combining all the different tech details according to the info
tech = eco_tech + buildings_tech + monastery_tech + infantry_tech + ranged_tech + cav_tech + ship_tech + misc_tech
tech_cost = eco_cost + buildings_cost + monastery_cost + infantry_cost + ranged_cost + cav_cost + ship_cost + misc_cost
tech_time = eco_time + buildings_time + monastery_time + infantry_time + ranged_time + cav_time + ship_time + misc_time
tech_effect = (
    eco_effect
    + buildings_effect
    + monastery_effect
    + infantry_effect
    + ranged_effect
    + cav_effect
    + ship_effect
    + misc_effect
)

# cleaning the data by removing space characters and whitespaces
escapes = "".join([chr(char) for char in range(1, 32)])
translator = str.maketrans("", "", escapes)

for i in range(0, len(tech_cost)):
    t = tech_cost[i].translate(translator)
    tech_cost[i] = t

for i in range(0, len(tech)):
    t = tech[i].translate(translator)
    tech[i] = t

for i in range(0, len(tech_effect)):
    t = tech_effect[i].translate(translator)
    tech_effect[i] = t

for i in range(0, len(tech_time)):
    t = tech_time[i].translate(translator)
    tech_time[i] = t

# Combining all the info for a particular technology in a single list (with some added formatting)
tech_info = []
for i in range(0, len(tech)):
    t = "Effect: " + tech_effect[i] + "; Cost: " + tech_cost[i] + "; Time to Research: " + tech_time[i]
    tech_info.append(t)

# further cleaning
for i in range(0, len(tech)):
    t = tech[i].replace("\xa0", " ")
    tech[i] = t
    tech[i] = tech[i].lower()
    sentence = re.sub(r"^\s+", "", tech[i], flags=re.UNICODE)
    tech[i] = sentence

# converting the two lists (Tech name, and tech info) into key value pairs using dictionary (tech names are in lowercase)

tech_all = dict(zip(tech, tech_info))
