from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from team_stats import Team_Stats
from selenium.webdriver.support.ui import Select
import time
import datetime as dt

def main():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    team_stats = Team_Stats(driver)
    team_stats.get_offense_team_stats()
    # driver.get("https://www.nfl.com/stats/team-stats/")
    # select = Select(driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
    # year = dt.datetime.today().year
    # years = list(range(year, year - 6, -1))
    # for i in years:
    #     select = Select(driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
    #     select.select_by_visible_text(str(i))
 

if __name__ == '__main__':
    main()