from analysis_covid_19.dataframes.state_dataframe import state_df
from datetime import datetime
from dateutil import tz


class PageData:
    current_date = datetime.utcnow().replace(tzinfo=tz.gettz('UTC')).astimezone(
        tz.gettz('America/Denver')).strftime('%B %d, %Y')
    cases = state_df[state_df.date == state_df.date.max()].cases.sum()
    deaths = state_df[state_df.date == state_df.date.max()].deaths.sum()
    latest_data_date = state_df.date.max().strftime('%B %d, %Y')


page_data = PageData()
