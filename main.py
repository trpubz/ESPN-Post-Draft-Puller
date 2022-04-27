# Scrape the ESPN Draft Results webpage and export data to JSON
# by pubins.taylor
# v1.0
# created 21APR2022
# instead of roster spot placement, just top 9 hitters and top 7 pitchers make the 'starting spots'
# TODO: import stat projections and sum stat
# lastUpdate 26APR2022

from TeamOffice import Team
from Player import Player
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By

teams: [Team] = []
playerUniverse: [Player] = []


def load_player_universe():
    """
    Opens a JSON file containing the eligible Player Universe, instantiates Player objects, appends those to local
    object.
    """
    with open("/Users/Shared/Baseball HQ/keysTRP.json", "r") as file:
        jsonData = json.load(file)
    print("loaded player universe")
    for i in jsonData:
        p = Player(espnid=i["idESPN"], fgid=i["idFangraphs"], name=i["name"], pos=i["pos"], tm=i["tm"])
        playerUniverse.append(p)


def driver_config() -> webdriver:
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver


def get_recap_html(leagueId: str) -> str:
    """
    Pulls down the HTML from the ESPN Draft Recap page.  Closes the driver upon completion.
    :param leagueId: a string representing the league ID in which one plays
    :return str: A string representing the HTML of Draft Recap Page
    """
    driver = driver_config()
    driver.get("https://fantasy.espn.com/baseball/league/draftrecap?leagueId=" + leagueId)
    driver.implicitly_wait(5)
    try:
        teamTables = driver.find_element(By.CSS_SELECTOR, "div.InnerLayout.flex.flex-auto.flex-wrap")\
            .get_attribute("outerHTML")
    except exceptions as e:
        print(e.message)
    print("pulled HTML!")
    driver.close()
    print("closed driver")
    return teamTables


def parse_tables(recap: str):
    """
    Parses the Draft Recap HTML and adds the Players to the Team's roster dictionary property.
    :param recap: the HTML for the Draft Recap
    """
    soup = BeautifulSoup(recap, features="lxml")
    teamTables = soup.select(".InnerLayout__child")
    for teamTable in teamTables:
        teamName = teamTable.find("span", {"class": "teamName truncate"}).get_text()
        tm = Team(name=teamName)
        playerTable = teamTable.find("tbody")
        for rowPlayer in playerTable.select("tr"):
            # a player has 3 table data elements; 1st is overall pick, 2nd is Player data, 3rd is draft value
            rowData = rowPlayer.select("td")
            # strip off the $ to get int
            draftValue = int(rowData[2].get_text().strip("$"))
            # Player data is segmented into 3 span elements, 1st is name, 2nd is team, 3rd is pos
            playerName = rowData[1].select("span")[0].get_text()
            # strip of characters and force uppercase
            playerTeam: str = rowData[1].select("span")[1].get_text().strip(", ").upper()
            for plyr in playerUniverse:
                if plyr.__eq__(other=(playerName, playerTeam)):
                    plyr.set_draft_details(tm=teamName, value=draftValue)
                    tm.add_player(plyr=plyr)
                    break

        teams.append(tm)


if __name__ == '__main__':
    load_player_universe()
    recap = get_recap_html(leagueId="10998")
    parse_tables(recap)
