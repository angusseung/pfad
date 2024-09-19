from bs4 import BeautifulSoup
import requests
import re

page_to_scrape = requests.get("https://store.steampowered.com/hwsurvey/cpus/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
stats = soup.findAll("div", attrs={"class": "substats_col_month"})
statValues = []
statTotals = []

for stat in stats:
    stat_text = stat.get_text().strip()
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", stat_text)

    if numbers:
        for number in numbers:
            statValues.append(float(number.replace('-', '0')))

for statValue in statValues:
    print(statValue)

for i in range(0, len(statValues), 4):
    total = sum(statValues[i:i+4])
    statTotals.append(total)
    
print(statTotals)