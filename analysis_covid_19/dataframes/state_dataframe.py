import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'


def get_state_dataframe() -> pd.DataFrame:
    """
    A function for generating a pandas dataframe from the New York Time's
    online csv file of covid-19 data for US states.
    :return: a pandas dataframe of US state covid-19 data
    :rtype: pd.DataFrame
    """
    df = pd.read_csv(url, parse_dates=['date'])
    df['death_rate'] = df['deaths'] / df['cases'] * 100
    return df


state_df = get_state_dataframe()
