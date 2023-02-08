from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Classes_To_Scrape_Data.offensive_stats import Offensive_Stats
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import datetime as dt
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utils import Utils
import pandas as pd

COLUMNS = "Team Win-Loss Win% MOV ATS"

options = webdriver.ChromeOptions()
# #options.add_argument("--headless")
# options.add_argument("--disable-gpu")
options.add_argument('ignore-certificates-errors')
options.add_argument("--window-size=1920x1080")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager('110.0.5481.30').install()), chrome_options = options)
driver.get('https://www.teamrankings.com/nfl/trends/win_trends/')
time.sleep(5)
select = Select(driver.find_element(By.XPATH, "//select[@id='range']"))



year = dt.datetime.today().year
#years = list(range(year-1, year - 19, -1))
years = range(year-1, 2010, -1)
all_data = []
for year in years:
    time.sleep(2)
    select = Select(driver.find_element(By.XPATH, "//select[@id='range']"))
    time.sleep(2)
    select.select_by_visible_text(str(year))
    time.sleep(3)
    table = driver.find_element(By.XPATH, "//tbody").text
    rows = table.split('\n')
    columns = COLUMNS.split(' ')
    data_rows = []
    for i in range(0, len(rows)):
        x = rows[i].split(' ')
        data_line = []
        # The following code catches case if team name has a space in the data
        if len(x) >= 6:
            data_line = [str(x[0]+ ' ' + x[1]), x[2], x[3], x[4], x[5]]
        else:
            data_line = [x[0], x[1], x[2], x[3], x[4]]
        data_rows.append(data_line)
        i += 1
    data = pd.DataFrame(data_rows, columns=columns)
    data["Year"] = year
    all_data.append(data)
all_data = pd.concat(all_data, axis = 0, ignore_index=True)
print(all_data)
#     data_rows.append(stat_line)
# table = pd.DataFrame(data_rows, columns=columns)
all_data.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/CSV_Data/' + 'Win_Loss' + '.csv'), index=False)

driver.close()
#table = driver.find_element(By.XPATH, '//tbody').text