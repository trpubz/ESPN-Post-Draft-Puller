# Scrape the ESPN Draft Results webpage and export data to JSON
# by pubins.taylor
# v0.3
# created 21APR2022
# loading Player Universe
# lastUpdate 24APR2022

from TeamOffice import Team
from Player import *
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions
from selenium.webdriver.common.by import By

teams: [Team] = []
players: [Player] = []


def load_Player_Universe():
    with open("/Users/Shared/Baseball HQ/keysTRP.json", "r") as file:
        jsonData = json.load(file)
    print("Datatype of variable: ", type(jsonData))
    print(jsonData)
    for i in jsonData:
        p = Player(espnid=i["idESPN"], fgid=i["idFangraphs"], name=i["name"], pos=i["pos"], tm=i["tm"])
        players.append(p)


def driver_config() -> webdriver:
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver


def get_recap_html(LeagueId: str) -> str:
    driver = driver_config()
    driver.get("https://fantasy.espn.com/baseball/league/draftrecap?leagueId=" + LeagueId)
    driver.implicitly_wait(5)
    try:
        teamTables = driver.find_element(By.CSS_SELECTOR, "div.InnerLayout.flex.flex-auto.flex-wrap")\
            .get_attribute("outerHTML")
    except exceptions as e:
        print(e.message)
    # print(teamTables)
    driver.close()
    return teamTables


def parse_tables(recap: str):
    soup = BeautifulSoup(recap, features="lxml")
    teamTables = soup.select(".InnerLayout__child")
    for team in teamTables:
        teamName = team.find("span", {"class": "teamName truncate"}).get_text()
        tm = Team(name=teamName)
        table = team.find("tbody")
        for rowPlayer in table.select("tr"):
            # a player has 3 table data elements; 1st is overall pick, 2nd is Player data, 3rd is draft value
            roundData = rowPlayer.select("td")
            # strip off the $ to get int
            draftValue = int(roundData[2].get_text().strip("$"))
            # Player data is segmented into 3 span elements, 1st is name, 2nd is team, 3rd is pos
            playerName = roundData[1].select("span")[0].get_text()
            # stip of characters and force uppercase
            playerTeam: str = roundData[1].select("span")[1].get_text().strip(", ").upper()
            for plyr in players:
                if plyr.__eq__(other=(playerName, playerTeam)):
                    plyr.set_draft_details(tm=teamName, value=draftValue)
                    tm.add_player(plyr=plyr, draftValue=draftValue)


        teams.append(tm)
        print(teamName)
    # print(len(teamTables))


if __name__ == '__main__':
    load_Player_Universe()
    recap = get_recap_html(LeagueId="10998")
    parse_tables(recap)
