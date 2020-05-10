from analysis_covid_19.plotting.plotting_state_data import state_df
import plotly.graph_objects as go


def plot_daily_new_us_cases() -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new cases of
    covid-19 for the US.  A rolling 7 day average is included.
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df.groupby('date').cases.sum().diff()
    data = data[data.index > '2020-02-29']
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Cases: </b>%{y:,}" +
                                               "<extra></extra>",
                                 marker={'color': 'blue', 'opacity': 0.4},
                                 name='Daily Cases')],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Cases for the US\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average',
                             marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig


def plot_daily_new_us_deaths() -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new deaths of
    covid-19 for the US.  A rolling 7 day average is included.
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df.groupby('date').deaths.sum().diff()
    data = data[data.index > '2020-02-29']
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Cases: </b>%{y:,}" +
                                               "<extra></extra>",
                                 marker={'color': 'blue', 'opacity': 0.4},
                                 name='Daily Deaths')],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Deaths for the US\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average', marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig
