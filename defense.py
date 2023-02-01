from pyexpat import native_encoding
import pandas as pd
from selenium.webdriver.support.ui import Select
import datetime as dt
from selenium.webdriver.common.by import By
from utils import Utils
import os

class Defense():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.nfl.com/stats/team-stats/")
    
    @staticmethod
    def defense_columns():
        PASSING_COLUMNS = "Team Att Cmp Cmp% Yds/Att PassYds TD INT Rate 1st 1st% 20+ 40+ Lng Sck SckY"
        RUSHING_COLUMNS = "Team Att RushYds YPC TD 20+ 40+ Lng Rush_1st Rush_1st% Rush_FUM"
        DOWNS_COLUMNS = "Team 3rd_Att 3rd_Md 4th_Att 4th_Md Rec_1st Rec_1st% Rush_1st Rush_1st% Scrm_Plys"
        column_dict = {'Passing': PASSING_COLUMNS, 'Rushing': RUSHING_COLUMNS, 'Downs': DOWNS_COLUMNS}
        return column_dict