import plotly.graph_objects as go
import pandas as pd

#Create a folder named 'templates' in the same directory as this.
#The following code generates an example chloropleth map and exports as html into /templates/testmap.html
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)
fig.write_html("templates/testmap.html")


#testing HERE
#load the state data
df2 = pd.read_csv('stateInfo.csv')
df2 = df2.loc[df2['title'] == "Transportation and Material Moving Occupations"]

#template for the choropleth map
fig2 = go.Figure(data=go.Choropleth(
    locations=df2['statecode'], # Spatial coordinates
    z = df2['employment'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Total Jobs",

))

#get the occupation to generate the map
fig2.update_layout(
    title_text = 'Transportation and Material Moving Occupations',
    geo_scope='usa', # limit map scope to USA

)
#writes the file to the templates folder
fig2.write_html("templates/transportation.html" )