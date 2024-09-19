from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import re

page_to_scrape = requests.get("https://store.steampowered.com/hwsurvey/cpus/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

titles = soup.findAll("div", attrs={"class": "substats_col_left"})
stats = soup.findAll("div", attrs={"class": "substats_col_month"})

titleTexts = []
finalTitles = []
statValues = []
statTotals = []

for title in titles:
    titleTexts.append(title.text)

finalTitles = [text for text in titleTexts if "PHYSICAL" not in text]

for stat in stats:
    stat_text = stat.get_text().strip()
    stat_text = stat_text.replace('-', '0')

    numbers = re.findall(r"[+]?\d*\.\d+|\d+", stat_text)
    if numbers:
        for number in numbers:
            statValues.append(float(number))

for i in range(0, len(statValues), 4):
    total = sum(statValues[i:i+4])
    statTotals.append(total)

plt.pie(statTotals, labels = finalTitles)
plt.show() 