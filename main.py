from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def main():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.nfl.com/stats/team-stats/offense/passing/2022/reg/all")
    table = driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
    rows = table.split('\n')
    header = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
    header = header.split(' ')
    rows.pop(0)
    stat_rows = []
    i = 0
    while i < len(rows):
        team_line = []
        team_line.append(rows[i])
        i+=1
        for x in rows[i].split(' '):
            team_line.append(x)
        i+=1
        stat_rows.append(team_line)
    table = pd.DataFrame(stat_rows, columns= header)
    print(header)
    print(stat_rows)
    print(table)
    driver.quit()

if __name__ == '__main__':
    main()