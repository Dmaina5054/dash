import dash
import requests
import dash_core_components as dcc #graphs
import dash_html_components as html #html/browser interface
from dash.dependencies import Input,Output
import pandas as pd



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#creating flask app
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

#defining interface colors

get_header = 'https://'
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

#defining layout
#adding data components


app.layout = html.Div(children=[
    
    dcc.Input(out_url,value='',type='text'),
    
    html.Div(id='url_builder'),
    
    
    #graph object here
    
    
    html.H1("Dannielabs Dash"),
    dcc.Graph(id='test_graph',
              figure = {
                  'data':[
                      {'x':[1,2,3,4,5],'y':[18,13,10,20,23,24,30], 'type':'bar','name':'users'},
                      {'y':[1,2,3,4,5],'y':[12,13,17,18,21,23,28], 'type':'line', 'name':'age'},
                      
                  ],
                  
                  #defining layout 
                  
                  'layout':{
                      'title':'Weekly tweets analysis',
                  },
                 
              }),
    
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks = {str(year):str(year) for year in df['year'].unique()},
        step=None,
    )
    
   
    
])


#wrappers

@app.callback(
    Output(component_id='url_builder',component_property='children'),
    [Input(component_id='out_url',component_property='value')]
)

def build_url(real_url):
    real_url = get_header + real_url
    resp = requests.get(real_url).headers['Server']
    return "{}".format(resp)
    
   
   
   

if __name__ == "__main__":
    app.run_server(debug=False)
    
    
    #refactored
