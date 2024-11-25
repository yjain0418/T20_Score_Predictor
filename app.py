import sklearn
import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Prediction')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', ['Select Team'] + sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', ['Select Team'] + sorted(teams))

city = st.selectbox('Select city', ['Select City'] + sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0)

with col4:
    overs = st.number_input('Overs done', min_value=0.0, max_value=20.0, step=0.1)

with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)

last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

if st.button('Predict Score'):
    if batting_team == 'Select Team' or bowling_team == 'Select Team' or city == 'Select City':
        st.error("Please select valid teams and city.")
    else:
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs if overs > 0 else 0

        input_df = pd.DataFrame(
            {'batting_team': [batting_team], 
             'bowling_team': [bowling_team], 
             'city': [city], 
             'current_score': [current_score], 
             'balls_left': [balls_left], 
             'wickets_left': [wickets_left], 
             'crr': [crr], 
             'last_five': [last_five]})

        result = pipe.predict(input_df)
        st.header("Predicted Score - " + str(int(result[0])))
