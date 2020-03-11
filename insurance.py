import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


df = pd.read_csv('insurance.csv')

app = dash.Dash()
<<<<<<< HEAD
charges_option = []
for charges in df["charges"].unique():
    charges_option.append({'label': str(charges), 'value': charges})


app.layout = html.Div([dcc.Dropdown(id='column_picker', options=charges_option,
                                    value=df['charges'].min()),
                       dcc.Graph(id='scatterplot',
                                 figure=px.scatter(df, x="bmi", y="charges",
                                                   color="charges", title='cheapest fee and BMI')),

                       dcc.Graph(id='piechart',
                                 figure=px.pie(df, values='charges', names='region',
                                               color_discrete_sequence=px.colors.sequential.RdBu,
                                               title='Cheapest insurance fee by region')),

                       dcc.Graph(id='bargraph',
                                 figure=px.scatter(df, x=df['age'], y=df['charges'],
                                                   hover_data=[
                                                       'age', 'charges'],
                                                   height=650, title='cheapest insurance fee by age')),

                       dcc.Graph(id='piechart2',
                                 figure=px.pie(df, values='charges', names='age',
                                               color_discrete_sequence=px.colors.sequential.RdBu,
                                               title='Cheapest insurance fee by age')),

                       dcc.Graph(id='stacked bargraph',
                                 figure=px.bar(df, x="sex", y="charges",
                                               height=650,
                                               title='Gender that pays the least fee')),

                       dcc.Graph(id='grouped bargraph',
                                 figure=px.bar(df, x="sex", y="charges", color='smoker',
                                               barmode='group', height=650,
                                               title='Gender that pays the least fee')),

                       dcc.Interval(id='interval-component',
                                    interval=2000,
                                    n_intervals=0)




                       ])

@app.callback(Output("scatterplot", 'figure'),
              [Input('column_picker', 'value')])
def update_figure(selected_charges):
    filtered_df = df[df['charges'] == selected_charges]

    health = []

    for weight in filtered_df['bmi'].unique():
        df_by_bmi = filtered_df[filtered_df['bmi'] == weight]
        weight.append(go.Scatter(
            x=df_by_bmi['bmi'],
            y=df_by_bmi['charges'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=weight
        ))
    return {'data': health, 'layout':go.Layout(tittle='BMI vs charges',
                                     xaxis={'title': 'BMI'},
                                     yaxis={'title': 'Insurance Fee'})}
                                     
if __name__ == '__main__':
    app.run_server()
=======

colors = {'background':'#111111','text':'#7FDBFF'}


app.layout = html.Div([dcc.Graph(id='scatterplot', 
                    figure = px.scatter(df, x="bmi", y="charges", 
                            color="charges", title='cheapest fee and BMI')),
    
                    dcc.Graph(id='piechart', 
                    figure = px.pie(df, values='charges', names='region', 
                        color_discrete_sequence=px.colors.sequential.RdBu, 
                        title='Cheapest insurance fee by region')),

                    dcc.Graph(id='bargraph', 
                    figure = px.bar(df, x=df['age'], y=df['charges'],
                        hover_data=['age', 'charges'],
                        height=650, title='cheapest insurance fee by age')),

                    dcc.Graph(id='stacked bargraph',
                    figure = px.bar(df, x="sex", y="charges",
                        height=650, 
                        title='gender that pays the least fee')),    

                    dcc.Graph(id='grouped bargraph', 
                    figure = px.bar(df, x="sex", y="charges", color='smoker', 
                        barmode ='group', height=650, 
                        title='gender that pays the least fee')),   

                    dcc.Interval(id='interval-component', 
                                interval=2000,
                                n_intervals=0)




                    ])


            
if __name__ == '__main__':
    app.run_server()
>>>>>>> 91e2cee011d7450ca4ea3212a9a5a4b22ccefd37
