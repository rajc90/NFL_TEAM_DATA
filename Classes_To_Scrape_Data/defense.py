from pyexpat import native_encoding
import pandas as pd
from selenium.webdriver.support.ui import Select
import datetime as dt
from selenium.webdriver.common.by import By
from Classes_To_Scrape_Data.utils import Utils
import os

class Defense():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.nfl.com/stats/team-stats/")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Defense']").click()
    
    @staticmethod
    def defense_columns():
        DEF_PASSING_COLUMNS = "Team D-Pass_Att D-Pass_Cmp D-Pass_Cmp% D-Pass_Yds/Att D-Pass_Yds D-Pass_TD D-Pass_INT D-Pass_1st D-Pass_1st% D-Pass_Sck"
        DEF_RUSHING_COLUMNS = "Team D-Rush_Att D-Rush_Yds D-Rush_YPC D-Rush_TD D-Rush_1st D-Rush_1st%"
        #DEF_DOWNS_COLUMNS = "Team D-Down_3rd_Att D-Down_3rd_Md D-Down_4th_Att D-Down_4th_Md  D-Down_Rush_1st D-Down_Rush_1st% D-Down_Scrm_Plys"
        column_dict = {'Passing_Defense': DEF_PASSING_COLUMNS, 'Rushing_Defense': DEF_RUSHING_COLUMNS}
        return column_dict

    def retreive_info_to_csv(self, columns):
        data = self.get_stats(columns=columns)
        for type in data.keys():
            dataframe = data[type]
            dataframe.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/' + type + '.csv'), index=False)
        return data

    def get_stats(self, columns, timeframe = 10):
        column_dict = columns
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

    def navigate_to(self, stat_type):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{stat_type}']").click()