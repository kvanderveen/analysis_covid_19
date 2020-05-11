import streamlit as st
from analysis_covid_19.page_data.data import page_data
from analysis_covid_19.plotting.plotting_national_data import (
    plot_daily_new_us_cases, plot_daily_new_us_deaths)
from analysis_covid_19.plotting.plotting_state_data import (
    plot_daily_new_cases_by_state, plot_daily_new_deaths_by_state,
    plot_cases_by_state, plot_deaths_by_state)
from analysis_covid_19.plotting.plotting_county_data import (
    plot_daily_new_cases_by_county, plot_daily_new_deaths_by_county)
from analysis_covid_19.dataframes.county_dataframe import (
    get_counties, states_and_territories_list, states_list)
from analysis_covid_19.page_content.content import page_content


def main():
    generate_intro()
    generate_us_plots()
    generate_state_plots()
    generate_state_comparison_plots()
    generate_county_plots()
    generate_conclusion()


def generate_intro():
    st.title('COVID-19 Analysis')
    st.subheader(page_data.current_date)
    st.markdown(page_content.introduction)


def generate_us_plots():
    st.subheader(page_content.us_plots_text)
    include_ny_nj = st.checkbox('Include New York and New Jersey data?',
                                value=True)
    new_us_cases = plot_daily_new_us_cases(include_ny_nj)
    new_us_deaths = plot_daily_new_us_deaths(include_ny_nj)
    st.plotly_chart(new_us_cases)
    st.plotly_chart(new_us_deaths)


def generate_state_plots():
    st.subheader(page_content.state_plots_text)
    state = st.selectbox("State/Territory", states_and_territories_list)
    new_cases_by_state = plot_daily_new_cases_by_state(state)
    new_deaths_by_state = plot_daily_new_deaths_by_state(state)
    st.plotly_chart(new_cases_by_state)
    st.plotly_chart(new_deaths_by_state)


def generate_state_comparison_plots():
    st.subheader(page_content.state_comparison_plots_text)
    selections = st.multiselect("States/Territories",
                                states_and_territories_list,
                                default=['Colorado'])
    cases_by_state = plot_cases_by_state(selections)
    deaths_by_state = plot_deaths_by_state(selections)
    st.plotly_chart(cases_by_state)
    st.plotly_chart(deaths_by_state)


def generate_county_plots():
    st.subheader(page_content.county_plots_text)
    state = st.selectbox("State", states_list)
    counties = get_counties(state)
    county = st.selectbox("County", counties)
    cases_by_county = plot_daily_new_cases_by_county(county, state)
    deaths_by_county = plot_daily_new_deaths_by_county(county, state)
    st.plotly_chart(cases_by_county)
    st.plotly_chart(deaths_by_county)


def generate_conclusion():
    st.markdown(page_content.conclusion)
    st.markdown('-Kevin Vanderveen, MD')


if __name__ == '__main__':
    main()
