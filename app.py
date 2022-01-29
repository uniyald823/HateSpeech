import pandas as pd
import dash
import dash_html_components as html
import jupyterlab_dash
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px 
df = pd.read_csv("C:/Users/Drishya/final_list_for_algo.csv")
df
# create the Dash app
#app = dash.Dash()

# set up app layout
app = JupyterDash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Hate Speech Detection'),
    dcc.Dropdown(id='BM-dropdown',
                options=[{'label': x, 'value': x}
                        for x in df['Username'].unique()],
                 value='Akhilesh',
                 multi=False, clearable=True),
    dcc.Graph(id='bar-chart')
])


# set up the callback function
@app.callback(
    Output(component_id="bar-chart", component_property="figure"),
    [Input(component_id="BM-dropdown", component_property="value")],
)
def display_BM_composition(selected_BM):
    filtered_BM = df[df.Username == selected_BM]  # Only use unique values in column "BM_NAME" selected in dropdown

    barchart = px.bar(
        data_frame=filtered_BM,
        x="Label",
        opacity=0.9,
        barmode='group')

    return barchart

# Run local server
if __name__ == '__main__':
    app.run_server(mode='external')
    #app.run_server(debug=True, use_reloader=False)
