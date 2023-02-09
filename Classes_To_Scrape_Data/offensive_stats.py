
import pandas as pd
from selenium.webdriver.support.ui import Select
import datetime as dt
from selenium.webdriver.common.by import By
from Classes_To_Scrape_Data.utils import Utils
import os



class Offensive_Stats(Utils):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.nfl.com/stats/team-stats/offense/passing/2022/reg/all")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Offense']").click()
    
    @staticmethod
    def offense_columns():
        OFF_PASSING_COLUMNS = "Team O-Pass_Att O-Pass_Cmp O-Pass_Cmp% O-Pass_Yds/Att O-Pass_Yds O-Pass_TD O-Pass_INT O-Pass_Rate O-Pass_1st O-Pass_1st% O-Pass_20+ O-Pass_40+ O-Pass_Lng O-Pass_Sck O-Pass_SckY"
        OFF_RUSHING_COLUMNS = "Team O-Rush_Att O-Rush_RushYds O-Rush_YPC O-Rush_TD O-Rush_20+ O-Rush_40+ O-Rush_Lng O-Rush_1st O-Rush_1st% O-Rush_FUM"
        OFF_DOWNS_COLUMNS = "Team O-down_3rd_Att O-down_3rd_Md O-down_4th_Att O-down_4th_Md O-down_Rec_1st O-down_Rec_1st% O-down_Rush_1st O-down_Rush_1st% O-down_Scrm_Plys"
        column_dict = {'Off_Passing': OFF_PASSING_COLUMNS, 'Off_Rushing': OFF_RUSHING_COLUMNS, 'Off_Downs': OFF_DOWNS_COLUMNS}
        return column_dict
    
    def retreive_info_to_csv(self, columns):
        data = self.get_stats(columns=columns, timeframe = 18)
        for type in data.keys():
            dataframe = data[type]
            dataframe.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/CSV_Data' + type + '.csv'), index=False)
        return data

    def get_stats(self, columns, timeframe = 10):
        year = dt.datetime.today().year
        years = list(range(year-1, year - timeframe, -1))
        offensive_information = {}
        for type in columns:
            self.navigate_to(type.title())
            all_data = []
            for i in years:
                select = Select(self.driver.find_element(By.XPATH, "(//select[@class='d3-o-dropdown'])[1]"))
                select.select_by_visible_text(str(i))
                table = self.driver.find_element(By.XPATH, "//div[@class='d3-o-table--horizontal-scroll']").text
                data = Utils().get_stats(table, columns[type])
                data["Year"] = i
                all_data.append(data)
            all_data = pd.concat(all_data, axis = 0, ignore_index=True)
            offensive_information[type.title()] = all_data
        return offensive_information

    def navigate_to(self, stat_type):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{stat_type}']").click()