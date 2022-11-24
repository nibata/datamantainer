import flask
import plotly
import plotly.express as px
import pandas as pd
import json


def get_data_plotly_example(country:str="United Kingdom"):
    """ Genera los datos de un pandas dataframe y lo transforma en un gráfico de linea plotly

    Parameters
    ----------
    country : str, optional
        Nombre del pais del que se quiere obtener el grafico, por defecto "United Kingdom"

    Returns
    -------
    JSON
        estructura de datos necesaria para se interpretada por plotly y mostrar el gráfico en una vista
    """

    
    df = pd.DataFrame(px.data.gapminder())

    fig = px.line(df[df["country"]==country], x="year", y="gdpPercap")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
