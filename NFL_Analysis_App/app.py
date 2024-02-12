from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

team_records = pd.read_csv("NFL_Team_Records.csv")
offensive_stats = pd.read_csv("NFL_Offensive_Stats.csv")
defensive_stats = pd.read_csv("NFL_Defensive_Stats.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='______NFL_TEAM_DATA'),

    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['Pass_TD', 'Rush_TD', 'Pass Yds', 'INT'], value='Rush_TD', id='controls-and-radio-item'),
    dash_table.DataTable(data=offensive_stats.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
])



# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.bar(offensive_stats, x='Year', y=col_chosen)
    return fig


if __name__ == '__main__':
    app.run(debug=True)