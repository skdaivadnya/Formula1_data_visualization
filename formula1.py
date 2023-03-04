import dash
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
import glob
import plotly.express as px
from dash import Input, Output

app = dash.Dash(__name__)

path = 'downloads/formula1/'
all_files = glob.glob(path + "/*.csv")

                      
all_files             

list1 = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    list1.append(df)


df = pd.concat(list1, axis = 0, ignore_index = True)

print(df)

fig_1 = px.line(df, x="driverId", y="wins",  title ="Drivers are Competitive(Drivers vs. Wins)")

fig_2 = px.scatter(df, x="driverId", y="rank", title='Drivers are ranked better than previous seasons(Drivers vs. Rankings)')


fig_3 = px.line(df, x="qualifyId", y="position", title='Qualifying sessions are nailbiting than ever(Qualifying vs positions)')

fig_4 = px.scatter(df, x = "driverId", y = "laps", title='Most experienced drivers are on track now!(Drivers vs Laps done)')



fig_5= px.pie(df, names="driverId", values ="fastestLapTime",  title = "Cars are better than ever!(Drivers vs. Lap times)")


fig_6= px.pie(df, names="constructorRef", values ="points", title="Constructors have a better rivalry(Constructors vs. Points)")


fig_7 = px.scatter(df, x="year", y="raceId", title="Amazing race locations are back(Races vs Year)")
                      

fig_8= px.line(df, x="driverId", y="milliseconds", color="raceId", title="Pit stops are faster thus more action(Race vs Pitstops)")
                                                                                           


fig_9= px.pie(df, names="circuitRef", values ="driverRef", title="Less DNFs than the previous ERA (Circuits vs Drivers)")


fig_10= px.bar(df, x="driverStandingsId", y ="points", title="Furious Driver Rivalries(Drivers vs,)")


app.layout = html.Div(
    html.Div([
        html.H1('Why formula1 is interesting again after the era of Michael Schumacher?'),
        html.H4('Author : Ruthvik & Sanket'),
        html.P('use the range slider to change the values'),
        dcc.RangeSlider(min=df["wins"].min(),
                        max=df["wins"].max(),
                        value=[df["wins"].min(),
                               df["wins"].max()],
                        id='number_of_wins',
                        tooltip={"placement": "bottom"}
                        ),
        
        dcc.Graph(
            id='Graph1',
          
            ),
        dcc.Graph(
            id='Graph2',
            figure=fig_2
            ),
        
        dcc.Graph(
            id='Graph3',
            figure=fig_3
        ),
        dcc.Graph(
            id='Graph4',
            figure=fig_4
        ),
        dcc.Graph(
            id='Graph5',
            figure=fig_5
        ),
        dcc.Graph(
            id='Graph6',
            figure=fig_6
        ),
        dcc.Graph(
            id='Graph7',
            figure=fig_7
        ),
        dcc.Graph(
            id='Graph8',
            figure=fig_8
        ),
        dcc.Graph(
            id='Graph9',
            figure=fig_9
        ),
        dcc.Graph(
            id='Graph10',
            figure=fig_10
            
        ),
         ])
  
)
@app.callback(
    Output(component_id = 'Graph1', component_property = 'figure'),
    [Input(component_id = 'number_of_wins', component_property = 'value')])
def update_number_of_wins(adr_range):
    new_df= df(['wins'] >= adr_range[0]) & (
                df['wins'] <= adr_range[1])

    fig_1 = px.line(new_df, y='wins', x="driverId",
                       title='Drivers are Competitive(Drivers vs. Wins)',
                       )

    fig_1.update_layout(transition_duration=100)

    return fig_1
        

    


if __name__ == '__main__':
    app.run_server(debug=True)