from plotly.graph_objs import Layout, Scattergeo
from plotly import offline 
import pandas as pd 


# Import Excel sheet.
file = '/Users/mattnicholoff/python_projects/map_of_stock_exchanges/list_of_stock_exchanges.xlsx'
exchanges_df = pd.read_excel(file, 'Exchanges')
child_exchanges_df = pd.read_excel(file, 'Child Exchanges')


# Organize data. 
lons = exchanges_df['Longitude'].tolist()
lats = exchanges_df['Latitude'].tolist()
mkt_caps = exchanges_df['Market Cap (USD Trillions) '].tolist()


# Map the exchanges.
data = [{
	'type' : 'scattergeo',
	'lon' : lons,
	'lat' : lats,
	#text = ,
	'marker' : {
		'symbol' : 'diamond',
		'size': [3* cap for cap in mkt_caps],
		'sizemin' : 4 ,
		'color' : mkt_caps,
		'colorscale' : 'Bluered',
		'cmin' : 0,
		'cmax' : 25,
		'reversescale' : False,
		'colorbar': {'title':'Market Capitalization'},
		'line': {'color':'black'}
	},

}]

my_layout = {
	'title':'Global Stock Exchanges of Market Capitalization Over $500B',
	'geo': {
		'showcountries': True,
		#'lataxis_showgrid': True,
		#'lonaxis_showgrid': True,
		#'projection_type' : 'natural earth',
		'showcoastlines': True,
		'coastlinecolor': 'black',
		'showland': True,
		'landcolor': 'antiquewhite',
		'showocean' : True,
		'oceancolor' : 'lightsteelblue',
		'showlakes': True, 
		'lakecolor': 'lightsteelblue',
		#'showrivers': True,
		#'rivercolor': 'lightsteelblue',

		}
	}

fig = {'data':data , 'layout':my_layout}
offline.plot(fig, filename = 'global_stock_exchanges.html')






