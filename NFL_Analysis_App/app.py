from dash import Dash, html, dash_table
import pandas as pd

team_records = pd.read_csv("NFL_Team_Records.csv")
offensive_stats = pd.read_csv("NFL_Offensive_Stats.csv")
defensive_stats = pd.read_csv("NFL_Defensive_Stats.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Team Records From 2003 - 2023'),
    dash_table.DataTable(data=team_records.to_dict('records'), page_size=32),

    html.Div(children='Offensive Stats From 2003 - 2023'),
    dash_table.DataTable(data=offensive_stats.to_dict('records'), page_size=32),

    html.Div(children='Defensive Stats From 2003 - 2023'),
    dash_table.DataTable(data=defensive_stats.to_dict('records'), page_size=32)
])

if __name__ == '__main__':
    app.run(debug=True)