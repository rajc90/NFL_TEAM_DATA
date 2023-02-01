from pyexpat import native_encoding
import pandas as pd
from selenium.webdriver.support.ui import Select
import datetime as dt
from selenium.webdriver.common.by import By
from utils import Utils
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from offensive_stats import Offensive_Stats
from utils import Utils

def get_dataframes():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.nfl.com/stats/team-stats/")
    x = get_offense_team_stats(driver)
    driver.close()
    driver.quit()
    return x


@staticmethod
def offense_columns():
    PASSING_COLUMNS = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
    RUSHING_COLUMNS = "Team Att RushYds YPC TD 20+ 40+ Lng Rush_1st Rush_1st% Rush_FUM"
    DOWNS_COLUMNS = "Team 3rd_Att 3rd_Md 4th_Att 4th_Md Rec_1st Rec_1st% Rush_1st Rush_1st% Scrm_Plys"
    column_dict = {'Passing': PASSING_COLUMNS, 'Rushing': RUSHING_COLUMNS, 'Downs': DOWNS_COLUMNS}
    return column_dict

def retreive_info_to_csv():
    data = get_offense_team_stats()
    for type in data.keys():
        dataframe = data[type]
        dataframe.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/' + type + '.csv'), index=False)
    return data

def get_offense_team_stats(driver, timeframe = 10):
    column_dict = Offensive_Stats.offense_columns()
    year = dt.datetime.today().year
    years = list(range(year-1, year - timeframe, -1))
    offensive_information = {}
    for type in column_dict:
        driver = navigate_to(driver, type.title())
        all_data = []
        for i in years:
            select = Select(driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
            select.select_by_visible_text(str(i))
            table = driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
            data = Utils().get_stats(table, column_dict[type])
            data["Year"] = i
            all_data.append(data)
        all_data = pd.concat(all_data, axis = 0, ignore_index=True)
        offensive_information[type.title()] = all_data
    return offensive_information

def navigate_to(driver, stat_type):
    driver.find_element(By.XPATH, f"//a[normalize-space()='{stat_type}']").click()
    return driver

def get_stats(table, columns):
    rows = table.split('\n')
    header = columns.split(' ')
    rows.pop(0)
    stat_rows = []
    i = 0
    while i < len(rows):
        stat_line = []
        stat_line.append(rows[i])
        i+=1
        for x in rows[i].split(' '):
            stat_line.append(x)
        i+=1
        stat_rows.append(stat_line)
    table = pd.DataFrame(stat_rows, columns=header)
    return table

get_dataframes()