
import pandas as pd
from selenium.webdriver.support.ui import Select
import datetime as dt
from selenium.webdriver.common.by import By
from utils import Utils
import os



class Offensive_Stats(Utils):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.nfl.com/stats/team-stats/")
    
    @staticmethod
    def offense_columns():
        PASSING_COLUMNS = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
        RUSHING_COLUMNS = "Team Att RushYds YPC TD 20+ 40+ Lng Rush_1st Rush_1st% Rush_FUM"
        DOWNS_COLUMNS = "Team 3rd_Att 3rd_Md 4th_Att 4th_Md Rec_1st Rec_1st% Rush_1st Rush_1st% Scrm_Plys"
        column_dict = {'Passing': PASSING_COLUMNS, 'Rushing': RUSHING_COLUMNS, 'Downs': DOWNS_COLUMNS}
        return column_dict
    
    def retreive_info_to_csv(self):
        data = self.get_offense_team_stats()
        for type in data.keys():
            dataframe = data[type]
            dataframe.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/' + type + '.csv'), index=False)
        return data

    def get_offense_team_stats(self, timeframe = 10):
        column_dict = Offensive_Stats.offense_columns()
        year = dt.datetime.today().year
        years = list(range(year-1, year - timeframe, -1))
        offensive_information = {}
        for type in column_dict:
            self.navigate_to(type.title())
            all_data = []
            for i in years:
                select = Select(self.driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
                select.select_by_visible_text(str(i))
                table = self.driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
                data = Utils().get_stats(table, column_dict[type])
                data["Year"] = i
                all_data.append(data)
            all_data = pd.concat(all_data, axis = 0, ignore_index=True)
            offensive_information[type.title()] = all_data
        return offensive_information


    # def get_offense_team_stats(self, timeframe = 10):
    #     column_dict = Offensive_Stats.offense_columns()
    #     year = dt.datetime.today().year
    #     years = list(range(year-1, year - timeframe, -1))
    #     offensive_information = {}
    #     all_data = []
    #     for type in column_dict:
    #         self.navigate_to(type.title())
    #         for i in years:
    #             select = Select(self.driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
    #             select.select_by_visible_text(str(i))
    #             table = self.driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
    #             data = Utils().get_stats(table, column_dict[type])
    #             data["Year"] = i
    #             all_data.append(data)
    #     offensive_information = pd.concat(all_data, axis = 0)
    #         # offensive_information[type.title()] = all_data
    #     return offensive_information






    def navigate_to(self, stat_type):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{stat_type}']").click()