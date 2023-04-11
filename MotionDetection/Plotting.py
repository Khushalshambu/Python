from turtle import left

from folium import Tooltip
from MotionDetection import df 
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%M-%D %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%M-%D %H:%M:%S")


cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks = 1
p.sizing_mode = "scale_both"

hover = HoverTool(Tooltip=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="blue")

output_file("Graph1.html")
show(p)