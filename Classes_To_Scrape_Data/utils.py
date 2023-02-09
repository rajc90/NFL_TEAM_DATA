import pandas as pd

class Utils():
    def get_stats(self, table, columns):
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
    
    def to_csv(dataframe, title):
        dataframe.to_csv(str('C:/Users/rchap/Git/NFL_TEAM_DATA/' + title), index=False)
