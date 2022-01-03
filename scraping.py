import string
import requests
from bs4 import BeautifulSoup
import re

#reading fandom webpage using beautiful soup

soup = BeautifulSoup(requests.get('https://ageofempires.fandom.com/wiki/Technology_(Age_of_Empires_II)').content, 'lxml')

#finding required tables, using website and it's code

eco_tag = soup.find_all("table")[2]
eco_body = eco_tag.find_all('tbody')
eco_text = eco_tag.find_all('td')

buildings_tag = soup.find_all("table")[1]
buildings_body = buildings_tag.find_all('tbody')
buildings_text = buildings_tag.find_all('td')

monastery_tag = soup.find_all("table")[3]
monastery_body = monastery_tag.find_all('tbody')
monastery_text = monastery_tag.find_all('td')

infantry_tag = soup.find_all("table")[4]
infantry_body = infantry_tag.find_all('tbody')
infantry_text = infantry_tag.find_all('td')

ranged_tag = soup.find_all("table")[5]
ranged_body = ranged_tag.find_all('tbody')
ranged_text = ranged_tag.find_all('td')

cav_tag = soup.find_all("table")[6]
cav_body = cav_tag.find_all('tbody')
cav_text = cav_tag.find_all('td')

ship_tag = soup.find_all("table")[7]
ship_body = ship_tag.find_all('tbody')
ship_text = ship_tag.find_all('td')

misc_tag = soup.find_all("table")[8]
misc_body = misc_tag.find_all('tbody')
misc_text = misc_tag.find_all('td')

#declaring temporary variables for storing data fetched from tables
eco_cost = []
eco_time = []
eco_effect = []
eco_tech = []
eco_len = len(eco_text)

buildings_cost = []
buildings_time = []
buildings_effect = []
buildings_tech = []
buildings_len = len(buildings_text)

monastery_cost = []
monastery_time = []
monastery_effect = []
monastery_tech = []
monastery_len = len(monastery_text)

infantry_cost = []
infantry_time = []
infantry_effect = []
infantry_tech = []
infantry_len = len(infantry_text)

ranged_cost = []
ranged_time = []
ranged_effect = []
ranged_tech = []
ranged_len = len(ranged_text)

cav_cost = []
cav_time = []
cav_effect = []
cav_tech = []
cav_len = len(cav_text)

ship_cost = []
ship_time = []
ship_effect = []
ship_tech = []
ship_len = len(ship_text)

misc_cost = []
misc_time = []
misc_effect = []
misc_tech = []
misc_len = len(misc_text)

#fetching table data for Economic technologies
for i in range(3, eco_len, 6):
    eco_cost.append(eco_text[i].text)

for i in range(5, eco_len, 6):
    eco_time.append(eco_text[i].text)

for i in range(4, eco_len, 6):
    eco_effect.append(eco_text[i].text)

for i in range(0, eco_len, 6):
    eco_tech.append(str(eco_text[i].text))

#fetching table data for Building technologies
for i in range(3, buildings_len, 6):
    buildings_cost.append(buildings_text[i].text)

for i in range(5, buildings_len, 6):
    buildings_time.append(buildings_text[i].text)

for i in range(4, buildings_len, 6):
    buildings_effect.append(buildings_text[i].text)

for i in range(0, buildings_len, 6):
    buildings_tech.append(str(buildings_text[i].text))

#fetching table data for Monastery technologies
for i in range(3, monastery_len, 6):
    monastery_cost.append(monastery_text[i].text)

for i in range(5, monastery_len, 6):
    monastery_time.append(monastery_text[i].text)

for i in range(4, monastery_len, 6):
    monastery_effect.append(monastery_text[i].text)

for i in range(0, monastery_len, 6):
    monastery_tech.append(str(monastery_text[i].text))

#fetching table data for Infantry technologies
for i in range(3, infantry_len, 6):
    infantry_cost.append(infantry_text[i].text)

for i in range(5, infantry_len, 6):
    infantry_time.append(infantry_text[i].text)

for i in range(4, infantry_len, 6):
    infantry_effect.append(infantry_text[i].text)

for i in range(0, infantry_len, 6):
    infantry_tech.append(str(infantry_text[i].text))

#fetching table data for Ranged technologies
for i in range(3, ranged_len, 6):
    ranged_cost.append(ranged_text[i].text)

for i in range(5, ranged_len, 6):
    ranged_time.append(ranged_text[i].text)

for i in range(4, ranged_len, 6):
    ranged_effect.append(ranged_text[i].text)

for i in range(0, ranged_len, 6):
    ranged_tech.append(str(ranged_text[i].text))

#fetching table data for Cavalry technologies
for i in range(3, cav_len, 6):
    cav_cost.append(cav_text[i].text)

for i in range(5, cav_len, 6):
    cav_time.append(cav_text[i].text)

for i in range(4, cav_len, 6):
    cav_effect.append(cav_text[i].text)

for i in range(0, cav_len, 6):
    cav_tech.append(str(cav_text[i].text))

#fetching table data for Docks/ Ships technologies
for i in range(3, ship_len, 6):
    ship_cost.append(ship_text[i].text)

for i in range(5, ship_len, 6):
    ship_time.append(ship_text[i].text)

for i in range(4, ship_len, 6):
    ship_effect.append(ship_text[i].text)

for i in range(0, ship_len, 6):
    ship_tech.append(str(ship_text[i].text))

#fetching table data for misc technologies
for i in range(3, misc_len, 6):
    misc_cost.append(misc_text[i].text)

for i in range(5, misc_len, 6):
    misc_time.append(misc_text[i].text)

for i in range(4, misc_len, 6):
    misc_effect.append(misc_text[i].text)

for i in range(0, misc_len, 6):
    misc_tech.append(str(misc_text[i].text))

#combining all the different tech details according to the info
tech = eco_tech + buildings_tech + monastery_tech + infantry_tech + ranged_tech + cav_tech + ship_tech + misc_tech
tech_cost = eco_cost + buildings_cost + monastery_cost + infantry_cost + ranged_cost + cav_cost + ship_cost + misc_cost
tech_time = eco_time + buildings_time + monastery_time + infantry_time + ranged_time + cav_time + ship_time + misc_time
tech_effect = eco_effect + buildings_effect + monastery_effect + infantry_effect + ranged_effect + cav_effect + ship_effect + misc_effect

#cleaning the data by removing espace characters and whitespaces
escapes = ''.join([chr(char) for char in range(1, 32)])
translator = str.maketrans('', '', escapes)

for i in range(0,len(tech_cost)):
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

#Combining all the info for a particular technology in a single list (with some added formatting)
tech_info = []
for i in range(0, len(tech)):
    t = "Effect: " + tech_effect[i] + "; Cost: " + tech_cost[i] + "; Time to Research: " + tech_time[i]
    tech_info.append(t)

#further cleaning
for i in range(0, len(tech)):
    t = tech[i].replace(u'\xa0', ' ')
    tech[i] = t
    tech[i] = tech[i].lower()
    sentence = re.sub(r"^\s+", "", tech[i], flags=re.UNICODE)
    tech[i] = sentence

#converting the two lists (Tech name, and tech info) into key value pairs using dictionary (tech names are in lowercase)
tech_all = {}

for key in tech:
    for value in tech_info:
        tech_all[key] = value
        tech_info.remove(value)
        break
del tech_all["technology"]
print(tech_all)
