import flask
import plotly
import plotly.express as px
import pandas as pd
import json


def get_data_plotly_example(country="United Kingdom"):
    df = pd.DataFrame(px.data.gapminder())

    fig = px.line(df[df["country"]==country], x="year", y="gdpPercap")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
