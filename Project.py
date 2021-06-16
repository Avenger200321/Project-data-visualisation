import pandas as pandas
import plotly.express as plotly_express
File=pandas.read_csv('Copy+of+data+-+data.csv')
Chart=plotly_express.scatter(File,x='date',y='cases', color='country', )
Chart.show()