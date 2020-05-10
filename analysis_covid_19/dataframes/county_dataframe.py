from pathlib import Path
import pandas as pd
import json

abbreviation_path = Path(
    __file__).parent.parent.parent / 'state_abbreviations' / 'states.json'

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'


def get_state_abbreviations() -> dict:
    """
    A function for generating a dict of state names and their respective
    abbreviations from a json file.
    :return: a dict of state names and their respective abbreviations
    :rtype: dict
    """
    with open(abbreviation_path) as fp:
        abbreviations = json.load(fp)
        return abbreviations


def get_county_dataframe() -> pd.DataFrame:
    """
    A function for generating a pandas dataframe from the New York Time's
    online csv file of covid-19 data for US counties. Each county in the
    original dataset is amended to include the state abbreviation for clarity.
    :return: a pandas dataframe of US county covid-19 data
    :rtype: pd.DataFrame
    """
    abbreviations = get_state_abbreviations()
    df = pd.read_csv(url, parse_dates=['date'])
    df['county_state'] = df['county'] + ' (' + df['state'].apply(
        lambda x: abbreviations.get(x)) + ')'
    df['county_state'].fillna('Unknown', inplace=True)
    df['death_rate'] = df['deaths'] / df['cases'] * 100
    return df


def get_counties(state) -> list:
    """
    A function to obtain a list of counties for the counties dataframe that
    has been filtered by a state.
    :param state: a state of interest
    :type state: str
    :return: a list of unique counties
    :rtype: list
    """
    mask = county_df['state'] == state
    filtered_df = county_df[mask]
    return sorted(filtered_df['county'].unique())


county_df = get_county_dataframe()
states_and_territories_list = sorted(county_df['state'].unique())
territories = {'District of Columbia', 'Guam', 'Northern Mariana Islands',
               'Puerto Rico', 'Virgin Islands'}
states_list = sorted(set(states_and_territories_list).difference(territories))
