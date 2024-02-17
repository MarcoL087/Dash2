import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines='skip')

top_10_books = df.head(10)

fig = px.bar(top_10_books, 
             y='title', 
             x='  num_pages',
             title='Top 10 Books - Number of pages per title',
             orientation='h',
             labels={'  num_pages': 'Number of Pages'},
             height=600,
             width=1200)

fig.update_traces(marker_color='#fcba6f')

fig.update_layout(
    font_color='rgba(255, 255, 255, 0.9)',
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)' ,
    yaxis_title='',
    margin=dict(pad=25)
)

app = dash.Dash(__name__)


app.layout = html.Div(
    style={ 'background-image': 'url("/assets/background.jpg")',
        'background-size': 'cover',
        'background-position': 'center', 
        'flexDirection': 'column', 
        'alignItems': 'center', 
        'justifyContent': 'center', 
        'padding': '0 150px',
        'color': 'rgba(255, 255, 255, 0.9)'},
    
    children=[

        html.Img(src=app.get_asset_url('Resource-Page-Books-banner.png'), style={'width': '100%', 'max-width': '1300px'}),

        html.H1("Top 10 Books", style={'text-align': 'center', 'font-size': '36px', 'font-family': 'system-ui', 'margin': '30px'}),
        
        dcc.Graph(figure=fig, style={'background-color': 'transparent'}),

        
        html.Label("Select an author:", style={'font-family': 'system-ui', 'margin-top': '50px', 'margin-bottom': '50px'}),
        html.Label(""),
        dcc.Dropdown(
            id='author-dropdown',
            options=[{'label': author, 'value': author} for author in df['authors'].unique()],
            multi=True
        ),
        
        html.Label("Enter a maximum number of pages:",style={'font-family': 'system-ui', 'margin-top': '50px', 'margin-bottom': '50px'}),
        dcc.Input(
            id='max-pages-input',
            type='number',
            value=df['  num_pages'].max()
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
