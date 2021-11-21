import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.palettes import Spectral5
from bokeh.embed import components
from flask import Markup

class Beforeafter:
    def __init__(self):
            pass

    def top5():

        df18 = pd.read_csv('static/data/top5_18.csv')

        count18 = [df18['count'][i] for i in [4, 3, 2, 1, 0]]
        idx18 = [df18['category'][i] for i in [4, 3, 2, 1, 0]]
        source18 = ColumnDataSource(data=dict(category=idx18, count=count18, color=Spectral5))

        p18 = figure(y_range=idx18, x_range=(0, df18[['count']].values.max()),
                plot_width=600, plot_height=400, title="Top5 Category 20-21", tools="pan, wheel_zoom, box_zoom, reset")
        p18.hbar(y='category', right='count', height=0.8, source=source18, color='color', legend_field="category")
        p18.legend.location='bottom_right'
        p18.title.text_font_size = '15px'
        p18.axis.major_label_text_font_style = 'bold'

        script18, div18 = components(p18)
        script18 = Markup(script18)
        div18 = Markup(div18)

        # 20-21 top5
        df20 = pd.read_csv('static/data/top5_20.csv')

        count20 = [df20['count'][i] for i in [4, 3, 2, 1, 0]]
        idx20 = [df20['category'][i] for i in [4, 3, 2, 1, 0]]
        source20 = ColumnDataSource(data=dict(category=idx20, count=count20, color=Spectral5))

        p20 = figure(y_range=idx20, x_range=(0, df20[['count']].values.max()),
                plot_width=600, plot_height=400, title="Top5 Category 20-21", tools="pan, wheel_zoom, box_zoom, reset")
        p20.hbar(y='category', right='count', height=0.8, source=source20, color='color', legend_field="category")
        p20.legend.location='bottom_right'
        p20.title.text_font_size = '15px'
        p20.axis.major_label_text_font_style = 'bold'

        script20, div20 = components(p20)
        script20 = Markup(script20)
        div20 = Markup(div20)

        return script18, div18, script20, div20
