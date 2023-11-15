import pandas as pd
#Win_loss_data Cleaning
win_loss_data = pd.read_csv("C:/Users/rchap/Git/NFL_TEAM_DATA/CSV_Data/Win_Loss.csv")
win_loss_data[['Wins', 'Losses', 'Ties']] = win_loss_data['Win-Loss'].apply(lambda x: pd.Series(str(x).split('-')))
win_loss_data['Win%'] = win_loss_data['Win%'].apply(lambda x: pd.Series(str(x).replace('%','')))

win_loss_data.to_csv("C:/Users/rchap/Git/NFL_TEAM_DATA/CSV_Data/Win_Loss.csv", mode = 'w')



win_loss_data = pd.read_csv("C:/Users/rchap/Git/NFL_TEAM_DATA/CSV_Data/Win_Loss.csv")
