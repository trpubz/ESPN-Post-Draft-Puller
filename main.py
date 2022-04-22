# Scrape the ESPN Draft Results webpage and export data to JSON
# by pubins.taylor
# v0.2
# created 21APR2022
# lastUpdate 21APR2022

from Team import *
import Player
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions
from selenium.webdriver.common.by import By

teams: [Team]


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
    return teamTables
    driver.close()


def parse_tables(recap: str):
    soup = BeautifulSoup(recap, "lxml")
    soup.prettify()
    teamTables = soup.select(".InnerLayout__child")
    for team in teamTables:
        teamName = team.find("span", {"class": "teamName truncate"}).get_text()
        tm = Team(name=teamName)
        # TODO: create player objects from rows
        tm.roster[RosSpot.C] = Player()
        teams.append(tm)
        print(teamName)
    # print(len(teamTables))


if __name__ == '__main__': 
    recap = get_recap_html(LeagueId="10998")
    parse_tables(recap)
