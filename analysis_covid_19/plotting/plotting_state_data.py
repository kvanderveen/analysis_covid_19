from analysis_covid_19.dataframes.state_dataframe import state_df
import plotly.graph_objects as go


def plot_daily_new_cases_by_state(state='California') -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new cases of
    covid-19 for a particular state.  A rolling 7 day average is included.
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df[state_df.state == state].set_index('date')[
        'cases'].sort_index().diff()
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Cases: </b>%{y:,}" +
                                               "<extra></extra>",
                                 name='Daily Cases',
                                 marker={'color': 'blue', 'opacity': 0.4})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Cases for {state}\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average', marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig


def plot_daily_new_deaths_by_state(state='California') -> go.Figure:
    """
    A function that generates a plotly bar plot of daily new deaths of
    covid-19 for a particular state.  A rolling 7 day average is included.
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df[state_df.state == state].set_index('date')[
        'deaths'].sort_index().diff()
    moving_avg = data.rolling('7d').mean().round(0)
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>Date: </b>%{x}" +
                                               "<br><b>Deaths: </b>%{y:,}" +
                                               "<extra></extra>",
                                 name="Daily Deaths",
                                 marker={'color': 'blue', 'opacity': 0.4})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'Date'},
                                     title=f'\nDaily New Deaths for'
                                           f' {state}\n'))
    fig.add_trace(go.Scatter(x=moving_avg.index, y=moving_avg.values,
                             name='7 Day Average', marker={'color': 'blue'},
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>7 Day Avg: </b>%{y:,}" +
                                           "<extra></extra>", ))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig


def plot_cases_by_state(state_list=None) -> go.Figure:
    """
    A function that generates a plotly line plot (log scale on the y-axis)
    of cumulative covid-19 cases for selected state(s).
    :param state_list: the state(s) of interest
    :type state_list: list
    :return: a plotly figure object
    :rtype: go.Figure
    """
    if state_list is None:
        state_list = ['California', 'Arizona', 'Colorado']
    fig = go.Figure()
    for s in state_list:
        data = state_df[state_df.state == s].set_index('date').cases
        fig.add_trace(go.Scatter(x=data.index, y=data.values,
                                 hovertemplate=f"{s}" +
                                               "<br><b>Date: </b>%{x}" +
                                               "<br><b>Cases: </b>%{y:,}" +
                                               "<extra></extra>",
                                 marker={'opacity': 0.4}, name=s))
    fig.update_layout(yaxis={'title': 'Cumulative Cases (log scale)'},
                      xaxis={'title': 'Date'}, yaxis_type='log',
                      title=f'\nCumulative Cases\n', height=600, width=900,
                      showlegend=True)
    return fig


def plot_deaths_by_state(state_list=None) -> go.Figure:
    """
    A function that generates a plotly line plot (log scale on the y-axis)
    of cumulative covid-19 deaths for selected state(s).
    :param state_list: the state(s) of interest
    :type state_list: list
    :return: a plotly figure object
    :rtype: go.Figure
    """
    if state_list is None:
        state_list = ['California', 'Arizona', 'Colorado']
    fig = go.Figure()
    for s in state_list:
        data = state_df[state_df.state == s].set_index('date').deaths
        fig.add_trace(go.Scatter(x=data.index, y=data.values,
                                 hovertemplate=f"{s}" +
                                               "<br><b>Date: </b>%{x}" +
                                               "<br><b>Deaths: </b>%{y:,}" +
                                               "<extra></extra>",
                                 marker={'opacity': 0.4}, name=s))
    fig.update_layout(yaxis={'title': 'Cumulative Deaths (log scale)'},
                      xaxis={'title': 'Date'}, yaxis_type='log',
                      title=f'\nCumulative Deaths\n', height=600, width=900,
                      showlegend=True)
    return fig

# THE FUNCTIONS BELOW ARE NOT CURRENTLY BEING EMPLOYED IN THE APPLICATION


def plot_top_n_state_cases(n=10) -> go.Figure:
    """
    A function that generates a plotly bar plot of the case counts of
    covid-19 for the top n states.
    :param n: the number of states to include
    :type n: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df.groupby('state').cases.max().sort_values(ascending=False)[:n]
    date = state_df['date'].max().strftime('%B %d, %Y')
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>State: </b>%{x}" +
                                               "<br><b>Count: </b>%{y}" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'State'},
                                     title=f'\nCases in Top {n} US States '
                                           f'as of {date}\n'))
    fig.update_layout(height=600)
    return fig


def plot_top_n_state_deaths(n=10) -> go.Figure:
    """
    A function that generates a plotly bar plot of the death counts of
    covid-19 for the top n states.
    :param n: the number of states to include
    :type n: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df.groupby('state').deaths.max().sort_values(ascending=False)[
           :n]
    date = state_df['date'].max().strftime('%B %d, %Y')
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>State: </b>%{x}" +
                                               "<br><b>Count: </b>%{y}" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Count'},
                                     xaxis={'title': 'State'},
                                     title=f'\nDeath Counts in Top {n} US '
                                           f'States as of {date}\n'))
    fig.update_layout(height=600)
    return fig


def plot_top_n_state_death_rates(n=10) -> go.Figure:
    """
    A function that generates a plotly bar plot of the death rates of
    covid-19 for the top n states.
    :param n: the number of states to include
    :type n: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    mask = (state_df['date'] == state_df['date'].max()) & (state_df['cases'] > 1000)
    data = state_df[mask].sort_values('death_rate', ascending=False).set_index(
        'state')['death_rate'][:n].round(2)
    date = state_df['date'].max().strftime('%B %d, %Y')
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>State: </b>%{x}" +
                                               "<br><b>Rate: </b>%{y}%" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Rate (%)'},
                                     xaxis={'title': 'State'},
                                     title=f'\nDeath Rates in Top {n} States '
                                           f'as of {date}\n'))
    fig.update_layout(height=600)
    return fig


def plot_death_rate_by_state(state='California') -> go.Figure:
    """
    A function that generates a plotly line plot of the death rates from
    covid-19 over time for a particular state.
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df[state_df.state == state].groupby('date')[
        ['cases', 'deaths']].sum()
    data = data.deaths.div(data.cases).mul(100).round(2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data.values,
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>Rate: </b>%{y}%" +
                                           "<extra></extra>",
                             marker={'color': 'green', 'opacity': 0.4}, ))
    fig.update_layout(yaxis={'title': 'Rate (%)'}, xaxis={'title': 'Date'},
                      title=f'\n{state} Death Rate by Date\n', height=600)
    return fig


def plot_death_rate_for_us() -> go.Figure:
    """
    A function that generates a plotly line plot of the death rates from
    covid-19 over time for the US.
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_df.groupby('date')[['cases', 'deaths']].sum()
    data = data.deaths.div(data.cases).mul(100).round(2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data.values,
                             hovertemplate="<b>Date: </b>%{x}" +
                                           "<br><b>Rate: </b>%{y}%" +
                                           "<extra></extra>",
                             marker={'color': 'green', 'opacity': 0.4}, ))
    fig.update_layout(yaxis={'title': 'Rate (%)'}, xaxis={'title': 'Date'},
                      title=f'\nUS Death Rate by Date\n', height=600)
    return fig


def plot_days_from_case_to_death(n=10, smallest=False) -> go.Figure:
    """
    A function that generates a plotly bar plot of the number of days from
    the first case of covid-19 to the first death.
    :param n: the number of states to include in the plot
    :type n: int
    :param smallest: determines if the plot contains the states with the
    smallest of the greatest number of days
    :type smallest: bool
    :return: a plotly figure object
    :rtype: go.Figure
    """
    first_cases = state_df.groupby('state').date.min()
    first_deaths = state_df[state_df.deaths > 0].groupby('state').date.min()
    data = first_deaths.sub(first_cases).dropna().apply(
        lambda x: x.days).sort_values()
    data = data[:n] if smallest else data[-n:]
    fig = go.Figure(data=[go.Bar(x=data.index, y=data.values,
                                 hovertemplate="<b>State: </b>%{x}" +
                                               "<br><b>Days: </b>%{y}" +
                                               "<extra></extra>",
                                 marker={'color': 'green', 'opacity': 0.6})],
                    layout=go.Layout(yaxis={'title': 'Days'},
                                     xaxis={'title': 'State'},
                                     title=f'\nNumber of Days from First Case '
                                           f'to First Death\n'))
    fig.update_layout(height=600)
    return fig
