from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Classes_To_Scrape_Data.offensive_stats import Offensive_Stats
from Classes_To_Scrape_Data.defense import Defense

def main():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('ignore-certificates-errors')
    options.add_argument("--window-size=1920x1080")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # team_stats = Offensive_Stats(driver)
    # team_stats.retreive_info_to_csv(Offensive_Stats.offense_columns())
    def_team_stats = Defense(driver)
    def_team_stats.retreive_info_to_csv(Defense.defense_columns())
    driver.close()
    driver.quit()

 

if __name__ == '__main__':
    main()