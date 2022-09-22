from pyexpat import native_encoding
import pandas as pd
from selenium.webdriver.common.by import By
from utils import Utils

class Team_Stats(Utils):

    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.nfl.com/stats/team-stats/")
    
    def offense_columns(self):
        PASSING_COLUMNS = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
        RUSHING_COLUMNS = "Team Att RushYds YPC TD 20+ 40+ Lng Rush_1st Rush_1st% Rush_FUM"
        DOWNS_COLUMNS = "Team 3rd_Att 3rd_Md 4th_Att 4th_Md Rec_1st Rec_1st% Rush_1st Rush_1st% Scrm_Plys"
        column_dict = {'Passing': PASSING_COLUMNS, 'Rushing': RUSHING_COLUMNS, 'Downs': DOWNS_COLUMNS}
        return column_dict
    
    def defense_columns(self):
        PASSING_COLUMNS = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
        RUSHING_COLUMNS = "Team Att RushYds YPC TD 20+ 40+ Lng Rush_1st Rush_1st% Rush_FUM"
        DOWNS_COLUMNS = "Team 3rd_Att 3rd_Md 4th_Att 4th_Md Rec_1st Rec_1st% Rush_1st Rush_1st% Scrm_Plys"
        column_dict = {'Passing': PASSING_COLUMNS, 'Rushing': RUSHING_COLUMNS, 'Downs': DOWNS_COLUMNS}
        return column_dict
    
    def get_offense_team_stats(self):
        column_dict = self.offense_columns()
        for type in column_dict:
            self.navigate_to(type.title())
            table = self.driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
            x = Utils().get_stats(table, column_dict[type])
            x.to_csv(f"C:\\Users\\rchap\\Git\\NFL_TEAM_DATA\\{type.title()}_offense_data.csv")


    def navigate_to(self, stat_type):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{stat_type}']").click()