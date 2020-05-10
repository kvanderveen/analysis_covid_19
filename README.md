## Analysis COVID-19

A web-based application that utilizes the most recent 
covid-19 data available from the NYT covid-19 data 
[repository](https://github.com/nytimes/covid-19-data).
The application allows one to explore US covid-19 data
visually at the national, state and county levels.
An example of the deployed application can be found
[here](https://analysis-covid-19.herokuapp.com). Shout out to 
the creators of [Streamlit](https://docs.streamlit.io) 
for making it easy to build a web application for data 
science.


### Quick start

* Clone the repo: ```git clone https://github.com/kvanderveen/analysis_covid_19.git```
* cd into the directory: ```cd analysis_covid_19/```
* Install the requirements: ```pip install -r requirements.txt```
* Run the application: ```streamlit run app.py```

### What's included

Within the download you'll find the following directories and files.

```
analysis_covid_19/
├── LICENSE
├── Procfile
├── README.md
├── analysis_covid_19
│   ├── __init__.py
│   ├── dataframes
│   │   ├── __init__.py
│   │   ├── county_dataframe.py
│   │   └── state_dataframe.py
│   ├── page_content
│   │   ├── __init__.py
│   │   └── content.py
│   ├── page_data
│   │   ├── __init__.py
│   │   └── data.py
│   └── plotting
│       ├── __init__.py
│       ├── plotting_county_data.py
│       ├── plotting_national_data.py
│       └── plotting_state_data.py
├── app.py
├── requirements.txt
├── setup.sh
└── state_abbreviations
    └── states.json
```
In addition to the functions that are used to produce 
the plots, there are several other functions that can
be used to produce additional plots. These are 
contained in the plotting_county_data.py and
plotting_state_data.py files.

### Creators
##### Kevin Vanderveen
* https://github.com/kvanderveen

