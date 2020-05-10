from analysis_covid_19.page_data.data import page_data


class PageContent:
    introduction = (
        f"There are many excellent websites that provide updated covid-19 "
        f"data. Included among these sites is the [New York Times]"
        f"(https://www.nytimes.com/interactive/2020/us/coronavirus-us"
        f"-cases.html) interactive summary of the coronavirus outbreak. The "
        f"New York Times has made the covid-19 data they use publicly "
        f"available on [github](https://github.com/nytimes/covid-19-data). "
        f"On this site, we explore this data. It is hoped that this "
        f"exploration may prove useful to better understand this pandemic. At "
        f"the end of the day {page_data.latest_data_date}, there were "
        f"{page_data.cases:,} cases and {page_data.deaths:,} deaths in the US "
        f"due to covid-19. Negative values in the dataset can occur when a "
        f"state or county corrects an error in the number of cases or deaths "
        f"they've reported in the past, or when a state moves cases from one "
        f"county to another. Unusually large numbers on a particular date "
        f"represent a backlog of cases that were released on that date. The "
        f"code repository for this site can be found "
        f"[here](https://github.com/kvanderveen/analysis_covid_19). To "
        f"visualize the spread of covid-19 over time across the US, this "
        f"[site](https://covid-19-us-county-analysis.herokuapp.com) may be "
        f"helpful.")
    us_plots_text = (
        "The following 2 plots summarize the latest available data for daily "
        "covid-19 cases and deaths in the US.  Each solid line on the plots "
        "represents a 7 day average.")
    state_plots_text = (
        "The following 2 plots summarize the latest available data for "
        "covid-19 daily cases and daily deaths for a selected state/region. "
        "Each solid line on the bar plots represents a 7 day average. Select "
        "a state/territory below.")
    state_comparison_plots_text = (
        "The following 2 plots allow the selection of multiple US "
        "states/territories to compare cumulative covid-19 case and death "
        "counts. Note the use of the log scale on the y-axis. Select one or "
        "more states/territories by clicking in the window below.")
    county_plots_text = (
        "The following 2 plots summarize the latest available data for "
        "covid-19 daily cases and daily deaths for a selected county. Each "
        "solid line on the bar plots represents a 7 day average. Select a "
        "state and one of its counties below.")
    conclusion = (
        "In the worst global pandemic since the 1918-1919 Influenza Pandemic, "
        "we have one significant advantage that they did not have over a "
        "century ago, access to timely data. It is my sincere hope that we "
        "use this advantage to avoid many of the mistakes that were made that "
        "ultimately cost the lives of countless individuals.")


page_content = PageContent()
