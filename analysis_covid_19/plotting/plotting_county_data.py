from analysis_covid_19.dataframes.county_dataframe import county_df
import plotly.graph_objects as go


def plot_top_n_county_cases(n=10, include_unknown=True) -> go.Figure:
    """
    A function that generates a plotly bar plot of the case counts of
    covid-19 for the top n counties in the US.
    :param n: the number of counties to include
    :type n: int
    :param include_unknown: unknown counties are included in the dataset,
    setting include_unknown to True includes these unknown counties
    :type include_unknown: bool
    :return: a plotly figure object
    :rtype: go.Figure
    """
    if include_unknown:
        data = county_df.groupby('county').cases.max().sort_values(
            ascending=False)[:n]
    else:
        data = county_df.loc[
                   ~county_df['county'].str.contains('Unknown')].groupby(
            'county').deaths.max().sort_values(ascending=False)[:n]
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>County: </b>%{x}" +
                                               "<br><b>Count: </b>%{y}" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'County'},
                                     title=f'\nCases in Top {n} US '
                                           f'Counties\n'))
    fig.update_layout(height=600)
    return fig


def plot_top_n_county_deaths(n=10, include_unknown=True) -> go.Figure:
    """
    A function that generates a plotly bar plot of the death counts of
    covid-19 for the top n counties in the US.
    :param n: the number of counties to include
    :type n: int
    :param include_unknown: unknown counties are included in the dataset,
    setting include_unknown to True includes these unknown counties
    :type include_unknown: bool
    :return: a plotly figure object
    :rtype: go.Figure
    """
    if include_unknown:
        data = county_df.groupby('county').deaths.max().sort_values(
            ascending=False)[:n]
    else:
        data = county_df.loc[
                   ~county_df['county'].str.contains('Unknown')].groupby(
            'county').deaths.max().sort_values(ascending=False)[:n]
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>County: </b>%{x}" +
                                               "<br><b>Count: </b>%{y}" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'County'},
                                     title=f'\nDeath Counts in Top {n} US '
                                           f'Counties\n'))
    fig.update_layout(height=600)
    return fig


def plot_top_n_county_death_rates(n=10) -> go.Figure:
    """
    A function that generates a plotly bar plot of the death rates of
    covid-19 for the top n counties in the US.
    :param n: the number of counties to include
    :type n: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    mask = (county_df['date'] == county_df['date'].max()) & (
            county_df['cases'] > 1000)
    data = county_df[mask].sort_values('death_rate', ascending=False).set_index(
        'county')['death_rate'][:n].round(2)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>County: </b>%{x}" +
                                               "<br><b>Rate: </b>%{y}%" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Rate (%)'},
                                     xaxis={'title': 'County'},
                                     title=f'\nDeath Rates in Top {n} '
                                           f'Counties\n'))
    fig.update_layout(height=600)
    return fig


def plot_daily_new_cases_by_county(county: str, state: str) -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new cases of
    covid-19 for a particular county.  A rolling 7 day average is included.
    :param county: the county of interest
    :type county: str
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    mask = (county_df['state'] == state) & (county_df['county'] == county)
    filtered_df = county_df[mask]
    data = filtered_df.set_index('date')['cases'].sort_index().diff()
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Cases: </b>%{y:,}" +
                                               "<extra></extra>",
                                 name='Daily Cases',
                                 marker={'color': 'blue', 'opacity': 0.4})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Cases for {county} '
                                           f'County, {state}'
                                           f'\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average', marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig


def plot_daily_new_deaths_by_county(county: str, state: str) -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new cases of
    covid-19 for a particular county.  A rolling 7 day average is included.
    :param county: the county of interest
    :type county: str
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    mask = (county_df['state'] == state) & (county_df['county'] == county)
    filtered_df = county_df[mask]
    data = filtered_df.set_index('date')['deaths'].sort_index().diff()
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Deaths: </b>%{y:,}" +
                                               "<extra></extra>",
                                 name='Daily Cases',
                                 marker={'color': 'blue', 'opacity': 0.4})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Deaths for {county} '
                                           f'County, {state}'
                                           f'\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average', marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig
