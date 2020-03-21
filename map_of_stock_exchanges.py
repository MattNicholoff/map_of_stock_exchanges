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


# Map the exchanges.
data = [{
	'type' : 'scattergeo',
	'lon' : lons,
	'lat' : lats,

}]

my_layout = Layout(title='Global Stock Exchanges of Market Capitalization Over $500B')

fig = {'data':data , 'layout':my_layout}
offline.plot(fig, filename = 'global_stock_exchanges.html')

#print(exchanges_df.columns)